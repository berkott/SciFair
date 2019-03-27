import heartpy as hp
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter
from scipy.signal import find_peaks, periodogram
import numpy as np
import glob

class heart:
    def __init__(self):
        self.data = hp.get_data(glob.glob('../assets/new/*PPG.csv')[0], column_name='ppg_2')
        self.data = self.fixData(self.data)
        self.epoch = 64*30

    def fixData(self, fix):
        fixed = np.asarray(fix)
        mean = np.mean(fixed)
        return np.subtract(fixed, mean)

    def butter_bandpass(self, lowcut, highcut, fs, order=5):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        b, a = butter(order, [low, high], btype='band')
        return b, a

    def butter_bandpass_filter(self, data, lowcut, highcut, fs, order=5):
        b, a = self.butter_bandpass(lowcut, highcut, fs, order=order)
        y = lfilter(b, a, data)
        return y

    def calcBPM(self, data_period):
        # low cut, high cut, sampling rate (Hz), order
        results = self.butter_bandpass_filter(data_period, 1, 5, 64, order=6)
        _, measures = hp.process(results, 64)
        print("BPM: ", measures["bpm"])
        return measures["bpm"]

    def getResult(self):
        heartRates = []
        for i in range(int(len(self.data)/self.epoch)):
            heartRates.append(self.calcBPM(self.data[i*self.epoch:((i+1)*self.epoch)-1]))
        
        numberOver100 = 0
        for i in heartRates:
            if(i > 100):
                numberOver100 += 1
        percentOver100 = numberOver100/len(heartRates)

        score = 0
        
        if(percentOver100 < .3):
            score = 100*percentOver100*3
        else:
            score = (10/.7)*percentOver100+(100-(10/.7))

        print("Heart score: ", score)
        return score