# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 15:58:12 2021

@author: 23820
"""

candidates='ABCD'
for ch in candidates:
    count=0
    if ch!='A': count+=1
    if ch=='C': count+=1
    if ch=='D': count+=1
    if ch!='D': count+=1
    if count==3:
        print("罪犯是：",ch)
        break
