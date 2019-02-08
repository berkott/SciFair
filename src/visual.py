import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import numpy as np
import pandas as pd

df = pd.read_csv('assets/new/Muse.csv')

x = df['timestamps']
y = df['ppg_1']
# plt.xlim(3.5, 4.0)
plt.plot(x, y)
plt.show()
