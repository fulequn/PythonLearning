# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 18:55:37 2020

@author: 23820
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

np.random.seed(3)  #设置随机种子
df = pd.DataFrame(np.random.rand(15,4)*100, 
                  columns=['05121', '05122', '05123', '05124'])
#先生成0-1之间的5*4维度数据，再装入4列DataFrame中

#设置返回类型为字典类型
#当指定return_type=‘dict’时，其结果值为一个字典，字典索引为固定的'whiskers'、'caps'、'boxes'、'fliers'、'means'
f = df.boxplot(sym='r*',patch_artist=True,return_type='dict')
#设置颜色
for box in f['boxes']:
    # 箱体边框颜色
    box.set( color='#7570b3', linewidth=2)
    # 箱体内部填充颜色
    box.set( facecolor = '#1b9e77' )

# whiskers：须
# 箱线图的连线为红色
for whisker in f['whiskers']:
    whisker.set(color='r', linewidth=2)

#箱体内部的颜色
for cap in f['caps']:
    cap.set(color='g', linewidth=3)
#中位线的颜色
for median in f['medians']:
    median.set(color='DarkBlue', linewidth=3)
#异常值的标签
for flier in f['fliers']:
    flier.set(marker='o', color='y', alpha=0.5)
    
#设置中文字体
plt.rcParams['font.sans-serif']=['SimHei']  
plt.rcParams['axes.unicode_minus'] = False

plt.xlabel("班级号", fontsize=12)
plt.ylabel("成绩", fontsize=12)
plt.title("180512133付乐群-各班的可视化成绩", fontsize=15)

plt.show()
