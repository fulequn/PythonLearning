# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 22:46:43 2019

@author: 23820
"""

#!/usr/bin/python 3
# -*- coding: UTF-8 -*-

_Author_ = '麦地吃大米'
f= open('latex.log','r')
i= 0
chars = 0
for line in f.readlines():
    # print(i)
    # print(line)
    # print(len(line))
    # i+=1
    # 判断空行
    if not (len(line) == 1  and line[-1]=='\n') :
        i +=1
        chars += len(line)-1

avg = round(chars/i,0)
avg = int(avg)
print(avg)