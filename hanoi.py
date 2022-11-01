# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:20:41 2020

@author: 23820
"""
import time
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.pyplot import MultipleLocator

times = 0

def hanoi(a, b, c, num):
    '''
    a:初始柱，b:中间柱，c:最终柱，num:移动盘数
    将num个大小不同的圆盘从a以b为辅助移动到c
    '''
    global times
    if num == 1:#只有1个则直接移动
        #print(a+"——>"+c)#将a上的盘直接移动到c
        times = times+1
    else:
        hanoi(a, c, b, num-1)#将a上n-1个盘通过c移动到b
        #print(a+"——>"+c)#将a上的盘直接移动到c
        times = times+1
        hanoi(b, a, c, num-1)#再将b上的盘以a为辅助移动到c

if __name__ == "__main__":
    num = list(range(1, 20))
    count = []#次数
    time_use = []#时间
    for i in num:
        times = 0
        oldtime = time.time()
        hanoi('a', 'b', 'c', i)
        newtime = time.time()
        runtime = newtime-oldtime#获得运行时间（ms为单位）
        count.append(times)
        time_use.append(runtime)
    #print(ls)
    plt.figure(dpi=128, figsize=(10,6))
    plt.plot(num, count, linewidth=5)
    
    #设置图标标题，并给坐标轴加上标签
    #解决汉字乱码
    mpl.rcParams['font.sans-serif']=['SimHei']  #使用指定的汉字字体类型（此处为黑体）
    plt.title('不同盘数下的移动次数情况', fontsize=24)
    plt.xlabel("盘数/(个)", fontsize=14)
    plt.ylabel("移动次数/(次)", fontsize=14)
    x_major_locator=MultipleLocator(1)#把x轴的刻度间隔设置为1，并存在变量里
    ax=plt.gca()#ax为两条坐标轴的实例
    ax.xaxis.set_major_locator(x_major_locator)#把x轴的主刻度设置为1的倍数

    # plt.show()
    plt.savefig("hanoi_count.png", bbox_inches='tight')
    
    
    # time_use = map(time_use, lambda x: x/1000)#将时间转化为s
    plt.figure(dpi=128, figsize=(10,6))
    plt.plot(num, time_use, linewidth=5)
    
    #设置图标标题，并给坐标轴加上标签
    #解决汉字乱码
    mpl.rcParams['font.sans-serif']=['SimHei']  #使用指定的汉字字体类型（此处为黑体）
    plt.title('不同盘数下的运行时间情况', fontsize=24)
    plt.xlabel("盘数/(个)", fontsize=14)
    plt.ylabel("运行时间/(ms)", fontsize=14)
    x_major_locator=MultipleLocator(1)#把x轴的刻度间隔设置为1，并存在变量里
    ax=plt.gca()#ax为两条坐标轴的实例
    ax.xaxis.set_major_locator(x_major_locator)#把x轴的主刻度设置为1的倍数

    # plt.show()
    plt.savefig("hanoi_time.png", bbox_inches='tight')
        