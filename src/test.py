from IPython.display import display
import matplotlib.pyplot as plt
import numpy as np
import os
import shutil
from scipy.signal import butter, lfilter
from scipy.signal import freqz
import wfdb
from butterworth import Butter


raw_data, _ = wfdb.rdsamp('../mitEEGData/slp01a', channels=[2])

display(_)

def butter_bandpass(lowcut, highcut, fs, order):
    print("lowcut: " + str(lowcut))
    print("highcut: " + str(highcut))

    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs):
    b, a = butter_bandpass(lowcut, highcut, fs, 5)
    print(data.shape)
    y = lfilter(b, a, data)
    print(y)
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

    for i in range(len(bands)):
        print("\n====="+str(i)+"=====")
        y = butter_bandpass_filter(raw_data.flatten(), bands[i][0], bands[i][1], fs)
        results.append(y.flatten())

    show(results)

    epochLength = 30*250
    epochResults = []

    resultLength = len(results[0])

    for i in range(len(bands)):
        epochResults.append(results[i].reshape(int(resultLength/epochLength), epochLength))

    print("\n=======Epoch Results=======")
    print(epochResults)

    minVal, maxVal, avgEnergy = getFeatures(epochResults, int(resultLength/epochLength))
    
    print("\n=======Extraction Results=======")
    
    print("\n=======min=======")
    print(minVal)
    print(minVal[0].shape)
    print("\n=======max=======")
    print(maxVal)
    print("\n=======avgEnergy=======")
    print(avgEnergy)

    
    
    # print(results)

def getFeatures(data, length):
    minVal = []
    maxVal = []
    energy = []

    for i in range(5):
        results = np.zeros(length)
        for j in range(length):
            results[j] = np.amin(data[i][j])
        minVal.append(results)

    for i in range(5):
        results = np.zeros(length)
        for j in range(length):
            results[j] = np.amax(data[i][j])
        maxVal.append(results)

    for i in range(5):
        results = np.zeros(length)
        for j in range(length):
            results[j] = np.sum(np.absolute(data[i][j]))
        energy.append(results)
    
    return minVal, maxVal, energy

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
