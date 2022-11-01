# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 13:10:54 2020

@author: 23820
"""
#scatter_squares.py

import matplotlib.pyplot as plt


#x_values = [1, 2, 3, 4, 5]
#y_values = [1, 4, 9, 16, 25]
#自动计算
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]#列表生成器

#plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)
#这里的c代表color，RGB模式

#使用颜色映射
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

#设置图标标题并给坐标轴加上标签
plt.title('Square Numbers', fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

#设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
plt.savefig('square_plot.png', bbox_inches='tight')
