# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 13:56:09 2021

@author: 23820
"""

from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

import numpy as np

#设置x轴取值
xedges = np.array([10,20,30,40,50,60,70])
#设置y轴取值
yedges = np.array([10,20,30,40,50,60,70])
#设置X,Y对应点的值。即原始数据。
hist =np.array( [[0.0964,0.1024,0.1043,0.1057,0.1072,0.1100],
[0.1027,0.1039,0.1057,0.1069,0.1078,0.1109],
[0.1046,0.1059,0.1061,0.1079,0.1085,0.1114],
[0.1068,0.1079,0.1084,0.1091,0.1096,0.1127],
[0.1091,0.1089,0.1107,0.1112,0.1118,0.1131],
[0.1102,0.1113,0.1121,0.1129,0.1133,0.1157]])

#生成图表对象。
fig = plt.figure()
#生成子图对象，类型为3d
ax = fig.add_subplot(111,projection='3d')

#设置作图点的坐标
xpos, ypos = np.meshgrid(xedges[:-1]-2.5 , yedges[:-1]-2.5 )
xpos = xpos.flatten('F')
ypos = ypos.flatten('F')
zpos = np.zeros_like(xpos)


#设置柱形图大小
dx =5 * np.ones_like(zpos)
dy = dx.copy()
dz = hist.flatten()

#设置坐标轴标签
ax.set_xlabel('node number')
ax.set_ylabel('experiment group number')
ax.set_zlabel('Pods number')

ax.bar3d(xpos, ypos, zpos, dx, dy, dz,color='b',zsort='average',alpha=0.8)

plt.show()

