# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 14:11:21 2020

@author: 23820
"""
#txtReaderV0.py

import re
import matplotlib as mpl
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np

host_utilization_different=defaultdict(list)
hud=defaultdict(str)
#处理每一句话
def useful(s):
    b = (s in '#.%]0123456789')
    return b

def readCloudSimTxt(filepath):
    vm = []
    host = []
    with open(filepath) as fl:
        #fl = filter(useful, fl)
        for line in fl:
            
            if '%' in line and 'Host' in line :
                #print(line)
                '''fl = filter(useful, line)
                ls = list(fl)
                s = "".join(ls)'''
                ls = re.split('[\[\]]', line)
                ls[0] = ls[0][:-2]
                
                utilization = ls[2].split()[-1]
                utilization = utilization.replace('(','')
                utilization = utilization.replace(')','')
                
                host_utilization_different[ls[0]].append(utilization)
                del ls[2]
                ls.append(utilization)
                st = "  ".join(ls)
                host.append(st)
            elif '%' in line and 'VM' in line:
                '''
                fl = filter(useful, line)
                ls = list(fl)
                s = "".join(ls)
                '''
                ls = re.split('[\[\]]', line)
                utilization = ls[2].split()[-1]
                utilization = utilization.replace('(','')
                utilization = utilization.replace(')','')
                del ls[2]
                ls.append(utilization)
                st = "  ".join(ls)
                vm.append(st)
    return host, vm



host, vm = readCloudSimTxt("D:\\自己用\\项目\\Python\\cloudsim\\random_iqr_mc_1.5.txt")
#print(host)
'''
with open("D:\\usage.txt", 'w+') as f:
    for line in host:
        f.write(line+'\n')
    for line in vm:
        f.write(line+'\n')
'''       
time = []
util = []


#数据可视化
factor = 2000#组内间隔
line_sum = 0.0
length = 0
for k,v in host_utilization_different.items():
    
    key = int(float(k)/factor)
    if key not in hud.keys():
        line_sum = 0.0
        length = 0
    else:
        pass
    for value in v:
        line_sum += float(value[:-1])
    length += len(v)
    mean = line_sum/length
    #mean = '{:.2f}%'.format(mean)
    hud[key] = mean#取1000ms内的最后一个点


for k,v in hud.items():
    time.append(k)
    util.append(v)

'''
x = hud.keys()       
y = np.array(hud.values())
''' 
#解决汉字乱码
mpl.rcParams['font.sans-serif']=['SimHei']  #使用指定的汉字字体类型（此处为黑体）
plt.xlabel("时刻/"+str(factor)+'ms')#横轴标识
plt.ylabel('服务器的平均利用率/(以%表示)')#纵轴标识
plt.plot(util, 'b')      #b代表用蓝色曲线
plt.title('不同时刻下，服务器的平均利用率画图')
#显示图形
plt.show()
  

'''
s = '6014.02: [Host #12] utilization is 0.00%'
#f = filter(useful, '6014.02: [Host #12] utilization is 0.00%')
ls = re.split('[\[\]]', s)
utilization = ls[2].split()[-1]
del ls[2]
ls.append(utilization)
st = "  ".join(ls)
print(st)

l = list(f)
s = "".join(l)
print(s)
#for i in f:
#    print(i)
f = filter(useful, '12asdf3456%')
for i in f:
    print(i)'''