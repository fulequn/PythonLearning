# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 21:07:19 2021

@author: 23820
"""

keyCount,rowCount = map(int, input().split())

keys=[i for i in range(1, keyCount+1)]
datas=[]
for i in range(rowCount):
    temp = list(map(int ,input().split()))
    datas.append([temp[0], temp[1], 1])
    datas.append([temp[0], temp[1]+temp[2], 2])

datas.sort(key = lambda temp:(temp[1], -temp[2], temp[0]))

for item in datas:
    if item[2]==1:
        keys[keys.index(item[0])] = 0
    else:
        keys[keys.index(0)] = item[0]

for item in keys:
    print(item, end=" ")
