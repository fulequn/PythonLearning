# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:26:29 2019

@author: 23820
"""
#differentSumV1.py
nums = input()
newnums = set(nums)
s = 0
for i in newnums:
    s = s+eval(i)
print(s)
