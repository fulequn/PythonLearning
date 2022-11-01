# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 22:19:58 2020

@author: 23820
"""
from matplotlib import pyplot as plt
import matplotlib as mpl
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

#防止中文乱码
mpl.rcParams['font.sans-serif']=['SimHei']  #使用指定的汉字字体类型（此处为黑体）
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

#给三个坐标轴注明
ax.set_xlabel('吞吐量x', color='r')
ax.set_ylabel('时延r', color='g')
ax.set_zlabel('效率k', color='b')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

