import heartpy as hp
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter
from scipy.signal import find_peaks, periodogram
import numpy as np
from PyEMD import EMD, Visualisation

# data1 = hp.get_data('../assets/testing/finalFilteredPPG.csv', column_name='ppg_1')
# data2 = hp.get_data('../assets/testing/finalFilteredPPG.csv', column_name='ppg_2')
# data3 = hp.get_data('../assets/testing/finalFilteredPPG.csv', column_name='ppg_3')

# data1 = hp.get_data('../assets/testing/outputBreathFinal.csv', column_name='ppg_1')
# data2 = hp.get_data('../assets/testing/outputBreathFinal.csv', column_name='ppg_2')
# data3 = hp.get_data('../assets/testing/outputBreathFinal.csv', column_name='ppg_3')

# data1 = hp.get_data('../assets/testing/finalPPG.csv', column_name='ppg_1')
# data2 = hp.get_data('../assets/testing/finalPPG.csv', column_name='ppg_2')
# data3 = hp.get_data('../assets/testing/finalPPG.csv', column_name='ppg_3')

data1 = hp.get_data('../assets/testing/holdingPPG.csv', column_name='ppg_1')
data2 = hp.get_data('../assets/testing/holdingPPG.csv', column_name='ppg_2')
data3 = hp.get_data('../assets/testing/holdingPPG.csv', column_name='ppg_3')

# data = hp.get_data('data/bidmc_01_Signals.csv', column_name='V')

def fixData(fix):
    fixed = np.asarray(fix)
    mean = np.mean(fixed)
    return np.subtract(fixed, mean)

data_1 = fixData(data1)
data_2 = fixData(data2)
data_3 = fixData(data3)

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

print(len(data1))
# for i in range(6):
# print("order: ", i)
# y = butter_bandpass_filter(data_2, .01, .3, 64, order=3)
y = butter_bandpass_filter(data_2, .13, .3, 64, order=3)
# getting breath
peaks, _ = find_peaks(y, distance=150)
plt.plot(peaks, y[peaks], "x")
# end breath

yb = butter_bandpass_filter(data_2, 1, 5, 64, order=6)
# plt.plot(np.arange(len(data1)), y, label='Filtered signal breath')
# plt.plot(np.arange(len(data1)), yb, label='Filtered signal heart')
# plt.plot(np.arange(len(data1)), data_1, label='Noisy signal 1')
plt.plot(np.arange(len(data_2)), data_2, label='Raw PPG 2')
# plt.plot(np.arange(len(data1)), data_3, label='Noisy signal 3')
plt.ylabel('some numbers')
plt.legend(loc='upper left')

plt.show()


# emd = EMD()
# emd.emd(y)
# imfs, res = emd.get_imfs_and_residue()

# In general:
#components = EEMD()(S)
#imfs, res = components[:-1], components[-1]

# vis = Visualisation()
# vis.plot_imfs(imfs=imfs, residue=res, t=np.arange(len(data1)), include_residue=True)
# vis.plot_instant_freq(np.arange(len(data1)), imfs=imfs)
# vis.show()

yp, den = periodogram(y, 64)

# power spectral density
maxPSD = max(den)

index = 0
for i in range(len(den)):
    if(den[i] == maxPSD):
        index = i

breathingRate = yp[index]*64
print("Breathing RATE: ", breathingRate)

plt.semilogy(yp, den)
# plt.ylim([1e-7, 1e2])
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.show()

print("Heart Rate:")
working_data, measures = hp.process(yb, 64)

print("BPM: ", measures["bpm"])

hp.plotter(working_data, measures)