import pandas as pd

class evaluate:
    def __init__(self):
        print("yay")

    def getResults(self, epworth, stopBang, weights):
        epScore = self.getEpworth(epworth)
        sbScore = self.getStopBang(stopBang)
        hrScore = self.getHeartRate()
        brScore = self.getBreathing()
        egScore = self.getEeg()

        totalScore = int(((egScore * weights['epworth']) + 
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
        return 50

    def getBreathing(self):
        return 50
    
    def getEeg(self):
        return 50
