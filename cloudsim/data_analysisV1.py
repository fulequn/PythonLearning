# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 17:53:43 2020

@author: 23820
"""
from collections import defaultdict
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#data_analysisV1.py
def getData(file):
    '''粗略提取数据'''
    energy = []#能耗数据
    utilization = []#服务器CPU利用率
    migration = []#迁移
    with open(file) as fl:
        for line in fl:
            if ": Data center's energy is " in line:
                energy.append(line)
            elif "] utilization is " in line:
                utilization.append(line)
            elif ": Migration of " in line and " is completed" in line:
                migration.append(line)
    return energy, utilization, migration


def analysis(energy, utilization, migration):
    en = analysisEnergy(energy)
    ut = analysisUtilization(utilization)
    mi = analysisMigration(migration)
    return en, ut, mi
    
#300.10: Data center's energy is 0.00 W*sec    
def analysisEnergy(energy):
    en = {}
    for line in energy:
        line = line.replace(" Data center's energy is ", "")
        line = line.replace(" W*sec\n", "")
        data = line.split(":")#分为两部分：时间和能耗
        en[data[0]] = data[1]
    return en
        

#300.10: [Host #20] utilization is 9.25%
def analysisUtilization(utilization):
    ut = defaultdict(list)#根据服务器来区分
    for line in utilization:
        line = line.replace(" [", "")
        line = line.replace(" utilization is ", "")
        line = line.replace("\n", "")
        data = line.split(":")#分为两部分：时间和 （主机+利用率）
        newdata = data[1].split("]")#主机，利用率
        h_u = {data[0]:newdata[1]}#时间：利用率
        ut[newdata[0]].append(h_u)
    return ut

#1227.94: Migration of VM #21 to Host #5 is completed
def analysisMigration(migration):
    mi = defaultdict(int)
    for line in migration:
        data = line.split(":")#分为两部分：时间和不重要的部分
        mi[data[0]] = mi[data[0]] + 1
    return mi
        

filename = "random_iqr_mc_1.5.txt"
energy, utilization, migration = getData(filename)
en, ut, mi = analysis(energy, utilization, migration)
# print(mi)
# # print(ut)
# #生成云计算中心的能耗情况图
# plt.figure(dpi=128, figsize=(10,6))
# # 隐藏坐标轴
# #解决汉字乱码
# mpl.rcParams['font.sans-serif']=['SimHei']  #使用指定的汉字字体类型（此处为黑体）
# plt.title('不同时刻下云计算中心的能耗情况', fontsize=24)
# plt.xlabel("时间/(ms)", fontsize=14)
# plt.ylabel("能耗/(W*sec)", fontsize=14)

# for k, v in en.items():
#     plt.scatter(float(k), float(v), c='#87CEFA',edgecolor='none', s=5)
# # plt.show()
# plt.savefig(filename[:-4]+k+"_energy.png", bbox_inches='tight')



# #生成不同时刻下不同服务器的利用率

# for k, v in ut.items():
#     plt.figure(dpi=128, figsize=(10,6))
#     # 隐藏坐标轴
#     #解决汉字乱码
#     mpl.rcParams['font.sans-serif']=['SimHei']  #使用指定的汉字字体类型（此处为黑体）
#     plt.title('不同时刻下'+k+'利用率情况', fontsize=24)
#     plt.xlabel("时间/(ms)", fontsize=14)
#     plt.ylabel("利用率/(%)", fontsize=14)
#     for l in v:
#         for k2, v2 in l.items():
#             plt.scatter(float(k2), float(v2[:-1]), c='#87CEFA',edgecolor='none', s=5)
#     # plt.show()
#     plt.savefig(filename[:-4]+k+"_utilization.png", bbox_inches='tight')



# #生成不同时刻的迁移次数的情况图
# plt.figure(dpi=128, figsize=(10,6))
# # 隐藏坐标轴
# #解决汉字乱码
# mpl.rcParams['font.sans-serif']=['SimHei']  #使用指定的汉字字体类型（此处为黑体）
# plt.title('不同时刻的迁移情况', fontsize=24)
# plt.xlabel("时间/(ms)", fontsize=14)
# plt.ylabel("次数/次", fontsize=14)

# for k, v in mi.items():
#     plt.scatter(float(k), int(v), c='#87CEFA',edgecolor='none', s=5)
# # plt.show()
# plt.savefig(filename[:-4]+"_migration.png", bbox_inches='tight')

                

#整个云数据中心的总能耗、平均CPU利用率、迁移次数。
sum_energy = 0.0#总能耗
#记得单位转换W*sec是每分的W，转化成W/ms（/（60*1000）），得到kW，然后转kWh（/60）
for v in en.values():
    sum_energy += float(v)
print("{:.2f}".format(sum_energy/(60*1000*60)) + "kWh")

sum_utilization = 0.0
count = 0
for k, v in ut.items():
    for l in v:
        for k2, v2 in l.items():
            sum_utilization += float(v2[:-1])
            count += 1
mean_utilization = sum_utilization/ count
print("{:.2f}".format(mean_utilization)+"%")

sum_migration = 0
for v in mi.values():
    sum_migration += int(v)
print(sum_migration+"次")


