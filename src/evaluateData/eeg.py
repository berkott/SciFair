from IPython.display import display
import matplotlib.pyplot as plt
import numpy as np
import os
import shutil
from scipy.signal import butter, lfilter
from scipy.signal import freqz
import wfdb
from butterworth import Butter
import glob
import os
import random
import pandas as pd
import heartpy as hp

# IGNORE THE ERRORS BELOW XDXDXD
import sys
sys.path.append("..")
from learningModels import ann
from learningModels import svm
from learningModels import knn
sys.path.remove("..")

# patient 48

class eeg:
    def __init__(self, model, fileN):
        self.EPOCH_LENGTH = 30*256
        # self.PERCENTAGE_TRAIN = 0.9
        self.rawData = hp.get_data(glob.glob('../assets/new/*EEG.csv')[0], column_name='eeg_2')
        # self.rawData, _ = wfdb.rdsamp("../../mitEEGData/slp" + fileN, channels=[2])
        self.fileN = fileN
        # 61, 37

        # Scores
        # ../../models/ann1553658225.h5
        #- 01a: 0.02
        #- 01b: 2.12
        #+ 02a: 61.57
        #- 02b: 45.23
        #- 03 , Score:  [26.90815]
        #+ 04 , Score:  [74.32257]
        #+ 14 , Score:  [90.28128]
        #+ 16 , Score:  [69.7211]
        #- 32 , Score:  [42.430088]
        #+ 37 , Score:  [75.68956]
        #- 41 , Score:  [0.58880097] 
        #+ 45 , Score:  [79.95658] wrong
        #- 48 , Score:  [5.6904535] wrong
        #+ 59 , Score:  [61.591255]
        #+ 60 , Score:  [55.05369]
        #- 61 , Score:  [29.133928]wrong
        #- 66 , Score:  [36.537632] wrong
        #- 67x , Score:  [0.45193583]

        # self._rawData = pd.read_csv(glob.glob('../assets/new/*EEG.csv')[0], 
        #                             skipinitialspace=False, usecols=["eeg_2"])
        # self.rawData = np.asarray(self._rawData)[1:]
        self.names = [
            "δ 0 – 4 Hz",
            "θ 4 – 8 Hz",
            "α 8 – 12 Hz",
            "β 12 – 22 Hz",
            "γ >30 Hz"
        ]
        self.bands = np.array([
            [1, 4],
            [4, 8],
            [8, 12],
            [12, 22],
            [22, 40]
        ])
        self.FS = 256
        self.EPOCH_LENGTH = 30 * self.FS
        self.model = model

    def butter_bandpass(self, lowcut, highcut, fs, order):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        b, a = butter(order, [low, high], btype='band')
        return b, a


    def butter_bandpass_filter(self, data, lowcut, highcut, fs):
        b, a = self.butter_bandpass(lowcut, highcut, fs, 5)
        # print(data.shape)
        y = lfilter(b, a, data)
        # print(y)
        return y

    def getFeatures(self, data):
        finalData = []

        numOfFeatures = 3
        for i in range(len(data[0])):
            period = np.zeros(numOfFeatures * 5)
            for j in range(len(data)):
                period[j*numOfFeatures] = np.amin(data[j][i])
                period[j*numOfFeatures + 1] = np.amax(data[j][i])
                period[j*numOfFeatures + 2] = np.sum(np.absolute(data[j][i]))
            finalData.append(period)

        return finalData

    def normalize(self, x):
        maxVal = np.amax(x)
        for i in range(len(x)):
            x[i] /= maxVal
        return x

    def getPrediction(self, x):
        prediction = 0
        if(self.model == "svm"):
            supportVectorMachine = svm.svm()
            supportVectorMachine.load()
            prediction = supportVectorMachine.predict(x)
        
        elif(self.model == "knn"):
            kNearestNeighbor = knn.knn()
            prediction = kNearestNeighbor.predict(x)

        else:
            #Default to ann
            artificialNeuralNetwork = ann.ann(0,0,0,0,0)
            # print(x)
            artificialNeuralNetwork.load()
            # print(artificialNeuralNetwork.predict(x[i]))
            prediction = artificialNeuralNetwork.predict(x)
        # print(prediction)

        return self.getScore(prediction[0])

    def getScore(self, prediction):
        score = 0

        if(prediction < .3):
            score = 100*prediction*3
        else:
            score = (10/.7)*prediction+(100-(10/.7))
        return score

    def getResult(self):
        results = []
        # print(np.asarray(self.rawData))
        for i in range(len(self.bands)):
            y = self.butter_bandpass_filter(self.rawData,
                            self.bands[i][0], self.bands[i][1], self.FS)
            results.append(y)
        
        # print(len(results))
        # print(len(results[0]))

        epochResults = []
        for i in range(len(results)):
            length = int(len(results[i])/self.EPOCH_LENGTH)*self.EPOCH_LENGTH
            # print(length)
            epochResults.append(results[i][:length].reshape(int(len(results[i])/self.EPOCH_LENGTH), 
                                                    self.EPOCH_LENGTH))
        
        featureVector = self.getFeatures(epochResults)
        normFeatureVector = self.normalize(np.array(featureVector))

        # print(normFeatureVector.shape)

        score = self.getPrediction(normFeatureVector)

        print(self.fileN, ", Score: ", score)

        return score[0]

names = [
    "01a",
    "01b",
    "02a",
    "02b",
    "03",
    "04",
    "14",
    "16",
    "32",
    "37",
    "41",
    "45",
    "48",
    "59",
    "60",
    "61",
    "66",
    "67x",
]

scores = []

actual = [
    0,
    0,
    1,
    0,
    1,
    1,
    1,
    1,
    0,
    1,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    0,
]

# for i in names:
eegN = eeg("ann", "_")
scores.append(eegN.getResult())

# correct = 0

# for i in range(len(actual)):
#     if(actual[i] == 0 and scores[i] < 30):
#         correct += 1
#     elif(actual[i] == 1 and scores[i] >= 30):
#         correct += 1

# print(correct/16)