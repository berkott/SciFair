from IPython.display import display
import matplotlib.pyplot as plt
import numpy as np
import os
import shutil
from scipy.signal import butter, lfilter
from scipy.signal import freqz
import wfdb
from butterworth import Butter
from learningModels import ann
import glob
import os
import random

# Nodes in input,Nodes in hidden,Epochs,Batch Size,Hidden Layers,Time,mse,accuracy

EPOCH_LENGTH = 30*250
PERCENTAGE_TRAIN = 0.90

def getXData():
    data = []
    list_of_files = glob.glob('../mitEEGData/*dat')
    for x in list_of_files:
        x_data, _ = wfdb.rdsamp(os.path.splitext(x)[0], channels=[2])
        display(_)
        if(os.path.splitext(x)[0] == "../mitEEGData/slp59"):
            data.append(x_data[22*250*30:])
        elif(os.path.splitext(x)[0] == "../mitEEGData/slp66"):
            data.append(x_data[:3292500])
        elif(os.path.splitext(x)[0] == "../mitEEGData/slp61"):
            data.append(x_data[150000:])
        elif(os.path.splitext(x)[0] == "../mitEEGData/slp14"):
            data.append(x_data[45000:])
        elif(os.path.splitext(x)[0] == "../mitEEGData/slp37"):
            data.append(x_data[15000:])
        elif(os.path.splitext(x)[0] == "../mitEEGData/slp16"):
            data.append(x_data[195000:])
        else:        
            data.append(x_data)

    return data


def getYData():
    print("========================")
    data = []

    list_of_files = glob.glob('../mitEEGData/*dat')
    
    for x in list_of_files:        
        thisFile = open(os.path.splitext(x)[0]+".txt")
        parts = []
        for i in thisFile:
            if("OA" in i or "X" in i):
                data.append(1)
                parts.append(1)
            else:
                data.append(0)
                parts.append(0)
        print(len(parts))
        
    return data

raw_data = getXData()
y_data = getYData()

print(len(y_data))
# print(len(y_data[0]))
    

def butter_bandpass(lowcut, highcut, fs, order):
    # print("lowcut: " + str(lowcut))
    # print("highcut: " + str(highcut))

    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs):
    b, a = butter_bandpass(lowcut, highcut, fs, 5)
    # print(data.shape)
    y = lfilter(b, a, data)
    # print(y)
    return y

names = [
    "δ 0 – 4 Hz",
    "θ 4 – 8 Hz",
    "α 8 – 12 Hz",
    "β 12 – 22 Hz",
    "γ >30 Hz"
]

def run():
    # Sample rate and desired cutoff frequencies (in Hz).
    fs = 250.0

    bands = np.array([
        [1, 4],
        [4, 8],
        [8, 12],
        [12, 22],
        [22, 40]
    ])
    results = []

    for j in range(len(raw_data)):
        layer = []
        for i in range(len(bands)):
            # print("\n====="+str(i)+"=====")
            y = butter_bandpass_filter(raw_data[j].flatten(), bands[i][0], bands[i][1], fs)
            layer.append(y.flatten())
        results.append(layer)

    print("\n=======Results=======")
    print(len(results))
    print(len(results[0]))
    print(len(results[0][0]))

    # show(results)
    epochResults = []

    for j in range(len(results)):
        layer = []
        for i in range(len(results[j])):
            resultLength = len(results[j][i])
            layer.append(results[j][i].reshape(int(resultLength/EPOCH_LENGTH), EPOCH_LENGTH))
        epochResults.append(layer)

    print("\n=======Epoch Results=======")
    # print(epochResults)

    featureVector = getFeatures(epochResults)  

    print("\n=======Feature Vector=======")

    print(len(y_data))
    print(len(featureVector))
    print(len(featureVector[0]))


    print("\n=======X DATA=======")
    print(featureVector[0])
    print("\n=======Y DATA=======")
    print(y_data[0])

    # print("\n=======X D=======")
    # print(xD[0])
    # print("\n=======Y D=======")
    # print(yD[0])

    # nii, nih, e, bs, hl
    # hyperparameters = [1, 1, 1, 64, 3]

    for i in range(1000):
        xD, yD = unison_shuffled_copies(np.array(featureVector), np.array(y_data))
        
        nodesInInput = random.randint(1,100)
        nodesInHidden = random.randint(1,100)
        epochs = random.randint(1,5)*1000
        # epochs = 100
        batchSize = random.randint(1,8)*16
        hiddenLayers = random.randint(1,4)

        neuralNet = ann.ann(nodesInInput, nodesInHidden, epochs, batchSize, hiddenLayers)
        neuralNet.createNetwork(15)
        # 10197 length
        neuralNet.train(xD[:int(10197*PERCENTAGE_TRAIN)], yD[:int(10197*PERCENTAGE_TRAIN)])
        neuralNet.save()
        neuralNet.evaluate(xD[int(10197*PERCENTAGE_TRAIN) + 1:], yD[int(10197*PERCENTAGE_TRAIN) + 1:])


def unison_shuffled_copies(a, b):
    randomize = np.arange(len(a))
    np.random.shuffle(randomize)
    return a[randomize], b[randomize]

def getFeatures(data):
    vector = []
    print(len(data))
    print(len(data[0]))
    print(len(data[0][0]))
    print(len(data[0][0][0]))
    print(data[0][0][0][0])

    print("\n==========data=========")

    for i in range(18):
        print(len(data[i][0]))
    # 18
    # 5
    # 270
    # 7500

    numOfFeatures = 3

    for k in range(len(data)):
        for i in range(len(data[k][0])):
            period = np.zeros(numOfFeatures * 5)
            for j in range(len(data[k])):
                period[j*numOfFeatures] = np.amin(data[k][j][j])
                period[j*numOfFeatures + 1] = np.amax(data[k][j][i])
                period[j*numOfFeatures + 2] = np.sum(np.absolute(data[k][j][i]))
            vector.append(period)
        
    return vector

def show(result):
    time = 2000

    plt.plot(np.arange(time), raw_data[:time], label='Original Signal')

    for i in range(len(result)):
        plt.plot(np.arange(time), result[i][:time], label=names[i])
        # plt.show()

    plt.xlabel('time (seconds)')
    # plt.hlines([-a, a], 0, T, linestyles='--')
    plt.grid(True)
    plt.axis('tight')
    plt.legend(loc='upper left')
    plt.show()

run()
