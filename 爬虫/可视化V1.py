# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 10:45:45 2019

@author: 23820
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = "D://title.csv"
match = pd.read_csv(path,encoding="gbk")
match.head()
match.sort_index(ascending= False ,by = '时间')
match.describe()
match.shape
match.dtypes
times = match['时间'].values
years = []
for time in times:
    years.append(int(time[0:4]))
match['年份'] = years
match.head()
match.sort_values(ascending= False,by= '年份')
match['年份'].value_counts()
counts = match['年份'].value_counts()
y = []
for count in counts:
    y.append(count)
    y = np.sort(y)
counts.head(100)
dframe = pd.DataFrame(match['年份'])
data = dframe.drop_duplicates()
years = []
years = data.values
data.sort_values(by='年份')
data = data.sort_values('年份')
plt.plot(data,y)
plt.xlabel('年份')
plt.ylabel('获奖数量')
plt.title('长春理工大学历年获奖情况')
plt.show()
