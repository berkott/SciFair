import heartpy as hp
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter
from scipy.signal import find_peaks, periodogram
import numpy as np
import glob

class breath:
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
        results = self.butter_bandpass_filter(data_period, .13, .3, 64, order=3)
        yp, den = periodogram(results, 64)

        # power spectral density
        maxPSD = max(den)

        index = 0
        for i in range(len(den)):
            if(den[i] == maxPSD):
                index = i

        breathingRate = yp[index]*64
        print("Breathing RATE: ", breathingRate)
        return breathingRate

    def getResult(self):
        breathRates = []
        for i in range(int(len(self.data)/self.epoch)):
            breathRates.append(self.calcBPM(self.data[i*self.epoch:((i+1)*self.epoch)-1]))
        
        numberOver100 = 0
        for i in breathRates:
            if(i < 8):
                numberOver100 += 1
        percentOver100 = numberOver100/len(breathRates)

        score = 0
        
        if(percentOver100 < .3):
            score = 100*percentOver100*3
        else:
            score = (10/.7)*percentOver100+(100-(10/.7))

        print("Breath score: ", score)
        return score