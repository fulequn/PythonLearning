# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 10:22:06 2021

@author: 23820
"""

money=int(input("请输入找零金额(1-99):"))

coins=(25,10,5,1)
counts=[]

for coin in coins:
    counts.append(money//coin)
    money%=coin
    
for i in range(len(counts)):
    print("找零{0}美分硬币{1}个".format(coins[i], counts[i]))