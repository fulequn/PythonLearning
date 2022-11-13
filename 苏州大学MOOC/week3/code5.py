# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 16:04:08 2021

@author: 23820
"""
values=(0,1)
candidates=[(A, B, C, D, E) for A in values
            for B in values
            for C in values
            for D in values
            for E in values]
for item in candidates:
    count=0
    if item[0]+item[1]==2 or item[0]==0:#AB都参加或者A没参加
        count+=1
    if item[1]+item[2]==1:#BC一人参加
        count+=1
    if item[2]==item[3]:#CD共进退
        count+=1
    if item[3]+item[4]>=1:#DE至少一人参加
        count+=1
    if item[0]+item[3]+item[4]==3 or item[4]==0: #EAD一起参加或E没参加
        count+=1
    if count==5:
        print(item)
        break