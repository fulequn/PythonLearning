# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 20:05:49 2020

@author: 23820
"""

import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.ticker import MultipleLocator, FormatStrFormatter 

#获取最大最小值
def minmax_value(list1):
    minvalue=min(list1)
    maxvalue=max(list1)
    return minvalue,maxvalue

#创建画布
plt.figure(figsize=(16,14),dpi=98)
xmajorLocator = MultipleLocator(1) #将x主刻度标签设置为1的倍数

#设置中文字体
plt.rcParams['font.sans-serif']=['SimHei']  
plt.rcParams['axes.unicode_minus'] = False

#生成1行2列的子图
p1 = plt.subplot(121)#第一行的左边
p2 = plt.subplot(122)#第一行的右边


#图中展示点的数量
pointcount=5

#生成数据
x=[i for i in range(20)]
print(x)
#生成数据
y1=[i**2 for i in range(20)]
y2=[i*4 for i in range(20)]
y3=[i*3+2 for i in range(20)]
y4=[i*4 for i in range(20)]

for i in range(len(x)-1):
    #如果不够展示点的数量
    if i<pointcount:
        minx,maxx=minmax_value(x[:pointcount])
        minx,maxx=minmax_value(x[:pointcount])
        minyA,maxyA=minmax_value(y1[:pointcount])
        minyB,maxyB=minmax_value(y2[:pointcount])
        
        maxy1=max(maxyA,maxyB)
        miny1=min(minyA,minyB)
        p1.axis([minx,maxx,miny1,maxy1])
        p1.grid(True)
        A,=p1.plot(x[:pointcount],y1[:pointcount],"g-")
        B,=p1.plot(x[:pointcount],y2[:pointcount],"b-")

        #设置主刻度标签的位置,标签文本的格式
        p1.xaxis.set_major_locator(xmajorLocator)
        legend=p1.legend(handles=[A,B],labels=["图1","图2"])    
        
        
        minx,maxx=minmax_value(x[:pointcount])
        minx,maxx=minmax_value(x[:pointcount])
        minyA,maxyA=minmax_value(y3[:pointcount])
        minyB,maxyB=minmax_value(y4[:pointcount])
        
        maxy1=max(maxyA,maxyB)
        miny1=min(minyA,minyB)
        p2.axis([minx,maxx,miny1,maxy1])
        p2.grid(True)
        A,=p2.plot(x[:pointcount],y3[:pointcount],"r-")
        B,=p2.plot(x[:pointcount],y4[:pointcount],"y-")

        #设置主刻度标签的位置,标签文本的格式
        p2.xaxis.set_major_locator(xmajorLocator)
        legend=p2.legend(handles=[A,B],labels=["图3","图4"])  
    elif i>=pointcount:
        minx,maxx=minmax_value(x[i-pointcount:i])
        minx,maxx=minmax_value(x[i-pointcount:i])
        minyA,maxyA=minmax_value(y1[i-pointcount:i])
        minyB,maxyB=minmax_value(y2[i-pointcount:i])
        
        maxy1=max(maxyA,maxyB)
        miny1=min(minyA,minyB)
        p1.axis([minx,maxx,miny1,maxy1])
        p1.grid(True)
        A,=p1.plot(x[i-pointcount:i],y1[i-pointcount:i],"g-")
        B,=p1.plot(x[i-pointcount:i],y2[i-pointcount:i],"b-")

        #设置主刻度标签的位置,标签文本的格式
        p1.xaxis.set_major_locator(xmajorLocator)
        legend=p1.legend(handles=[A,B],labels=["图1","图2"])

        minx,maxx=minmax_value(x[i-pointcount:i])
        minx,maxx=minmax_value(x[i-pointcount:i])
        minyA,maxyA=minmax_value(y3[i-pointcount:i])
        minyB,maxyB=minmax_value(y4[i-pointcount:i])
        
        maxy1=max(maxyA,maxyB)
        miny1=min(minyA,minyB)
        p2.axis([minx,maxx,miny1,maxy1])
        p2.grid(True)
        A,=p2.plot(x[i-pointcount:i],y3[i-pointcount:i],"r-")
        B,=p2.plot(x[i-pointcount:i],y4[i-pointcount:i],"y-")

        #设置主刻度标签的位置,标签文本的格式
        p2.xaxis.set_major_locator(xmajorLocator)
        legend=p2.legend(handles=[A,B],labels=["图3","图4"])


    #设置坐标轴标题以及图像的名称
    p1.set_xlabel("横轴属性名一",fontsize=14)
    p1.set_ylabel("纵轴属性名一",fontsize=14)
    p1.set_title("主题一",fontsize=18)
    
    p2.set_xlabel("横轴属性名二",fontsize=14)
    p2.set_ylabel("纵轴属性名二",fontsize=14)
    p2.set_title("主题二",fontsize=18)

    
    plt.pause(0.3)
    # 调用 plt.ion() 可以使能交互绘图功能. plt.show( ) 显示所绘制的图形
    # 调用 plt.pause(0.05) 不仅可以绘图而且鼠标可以继续交互
    plt.tight_layout(pad=4, w_pad=4.0, h_pad=3.0)
    # 功能:使得子图横纵坐标更加紧凑，主要用于自动调整图区的大小以及间距，使所有的绘图及其标题、坐标轴标签等都可以不重叠的完整显示在画布上。
    # 参数：
    # Pad:用于设置绘图区边缘与画布边缘的距离大小
    # w_pad:用于设置绘图区之间的水平距离的大小
    # H_pad:用于设置绘图区之间的垂直距离的大小