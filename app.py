# -*- coding: utf-8 -*-
"""

Author: lowdill

"""

import yahoo_fin.stock_info as yfin
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import date, timedelta

stDt = "12/04/2022"
stock_als = "^GSPC"
intTime = "1d"
tdyDt = date.today() + timedelta(days=-1)


# fetch data from yahoo finance
snp_test = yfin.get_data(stock_als, 
                         start_date=stDt, 
                         end_date=tdyDt, 
                         index_as_date = True, 
                         # interval="1wk")
                         interval=intTime)

snp_test['dateRef'] = pd.to_datetime(snp_test.index)

# snp_test['MACD'] = snp_test['close'].rolling(12).mean() #- snp_test['close'].rolling(26).mean()
snp_test['EMA12'] = snp_test['close'].ewm(span=12).mean()
snp_test['EMA26'] = snp_test['close'].ewm(span=26).mean()
snp_test['MACD'] = snp_test['EMA12'] - snp_test['EMA26']
snp_test['zeroInd'] = np.sign(snp_test['MACD']) == np.sign(snp_test['MACD'].shift())
snp_ref = snp_test[snp_test['zeroInd']==False]

# print(snp_ref)

f, (ax1, ax2) = plt.subplots(ncols=1, nrows=2, sharex=True)

sns.lineplot(x=snp_test['dateRef'], 
              y=snp_test['close'], 
              data=snp_test,
              color='blue',
              ax=ax1)
sns.lineplot(x=snp_test['dateRef'], 
              y=snp_test['EMA12'], 
              data=snp_test,
              color = 'red',
              ax=ax1)
sns.lineplot(x=snp_test['dateRef'], 
              y=snp_test['EMA26'], 
              data=snp_test,
              color = 'orange',
              ax=ax1)
plt.ylabel('SNP500')

sns.lineplot(x=snp_test['dateRef'], 
              y=snp_test['MACD'], 
              data=snp_test,
              color = 'blue',
              ax=ax2)
sns.lineplot(x=snp_test['dateRef'], 
              y=0,
              color='black',
              ax=ax2)
plt.vlines(x=snp_ref['dateRef'], 
           ymin=-60,
           ymax=60, 
           linestyle='dotted',
           linewidth = 0.8,
           color='red')
plt.ylabel('MACD Indicator')

plt.xticks(rotation=25)
plt.show()

# print(snp_test)
