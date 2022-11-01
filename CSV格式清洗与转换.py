ta# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 22:49:56 2019

@author: 23820
"""
#CSV格式清洗与转换.py
#!/usr/bin/python 3
# -*- coding: UTF-8 -*-

_Author_ = 'Sound_of_ Silence'

f = open('data.csv','r')
lines = f.readlines()
lines.reverse()

for line in lines:
    line = line.replace('\n','')
    line =line.replace(' ','')
    t = line.split(",")
    t.reverse()
    print(";".join(t))
