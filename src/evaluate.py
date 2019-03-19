# import keras as k
# from keras.models import Sequential
# from keras.layers import Dense, Activation
# from keras.optimizers import Adam
import numpy as np
import pandas as pd
from random import *
from learningModels import ann

class evaluate:
    def __init__(self):
        print("yay")
        pd.options.display.max_rows = 10
        pd.options.display.float_format = '{:.1f}'.format

    def getResults(self, epworth, stopBang, weights):
        epScore = self.getEpworth(epworth)
        sbScore = self.getStopBang(stopBang)
        hrScore = self.getHeartRate()
        brScore = self.getBreathing()
        egScore = self.getEeg()

        totalScore = int(((epScore * weights['epworth']) + 
                    (sbScore * weights['stopBang']) + 
                    (hrScore * weights['heartRate']) + 
                    (brScore * weights['breathing']) + 
                    (egScore * weights['eeg'])))
        
        return ({
            'score': totalScore,
            'heartRate': hrScore,
            'breathing': brScore,
            'eeg': egScore,
            'epworth': epScore,
            'stopBang': sbScore
            })

    def getEpworth(self, data):
        total = (data['ans1'] + data['ans2'] + data['ans3'] + data['ans4']
                + data['ans5'] + data['ans6'] + data['ans7'] + data['ans8'])
        return ((total / 24) * 100)

    def getStopBang(self, data):
        total = (data['ans1'] + data['ans2'] + data['ans3'] + data['ans4']
                + data['ans5'] + data['ans6'] + data['ans7'] + data['ans8'])
        return ((total / 8) * 100)

    def getHeartRate(self):
        result = randint(1, 10)
        return result

    def getBreathing(self):
        result = randint(5, 20)
        return result
    
    def getEeg(self):
        # neuralNet = ann.ann(nodesInInput, nodesInHidden, epochs, batchSize, hiddenLayers)
        
        
        # neuralNet.predict(data)
        
        result = randint(10, 30)
        return result
    