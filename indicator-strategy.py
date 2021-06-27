from nsepy import get_history
import pandas as pd
import numpy as np
import talib as ta
from datetime import date
import matplotlib.pyplot as plt

data=get_history(symbol="RELIANCE",start=date(2020,4,1),end=date(2021,2,1))

high = data['High']
low = data['Low']
close = data['Close']

ma=ta.MA(close,timeperiod=200)
sma20_list = np.ndarray.tolist(ma)
print(sma20_list)
AyDeXx = ta.ADX(high, low, close, timeperiod=14)
"""
plt.plot(AyDeXx)
plt.show()
"""

"""
buy = ta.EMA(close, timeperiod=20)
sell = ta.EMA(close, timeperiod=50)

for i in range(buy[close]):
	if buy[i]==sell[i]:
		print('B U Y')
	else:
		print('S E L L')
		"""
	    




