# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 16:23:00 2021

@author: 23820
"""

f = open('test.txt', 'rt')
date = f.readlines()
f.close()

dic = dict()
for line in date:
    line = line.upper()
    for c in line:
        if "A"<=c<="Z":
            dic[c] = dic.get(c,0)+1
i=0
for k in sorted(dic, key=dic.__getitem__, reverse=True):
    print("%s:%d\t" % (k, dic[k]), end='')
    i += 1
    if i%4 == 0:
        print('')
