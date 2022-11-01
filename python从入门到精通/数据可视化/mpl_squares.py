# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 19:05:00 2020

@author: 23820
"""
#mpl_squares.py

import matplotlib.pyplot as plt

#同时提供输入值和输出值
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

#设置图标标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)


plt.show()
