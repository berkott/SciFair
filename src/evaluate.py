import numpy as np
import pandas as pd
from random import *
from evaluateData import heart
from evaluateData import breath
from evaluateData import eeg

class evaluate:
    def __init__(self):
        print("yay")
        pd.options.display.max_rows = 10
        pd.options.display.float_format = '{:.1f}'.format

        self.heart = heart.heart()
        self.breath = breath.breath()
        self.eeg = eeg.eeg("ann", "_")
        

    def getResults(self, epworth, stopBang, weights):
        epScore = self.getEpworth(epworth)
        sbScore = self.getStopBang(stopBang)
        hrScore = self.heart.getResult()
        brScore = self.breath.getResult()
        egScore = self.eeg.getResult()

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