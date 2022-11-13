# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 20:50:03 2021

@author: 23820
"""

PI = 3.141592654
base = 1

for k in range(1, 8):
    base *= 10
    pi = 0
    tm = 1
    for i in range(0, base):
        pi += tm/(2*i+1)
        tm = -tm
    pi *= 4
    print("%d\tpi=%.7f\t误差率(*10000)=%.5f" % (k ,pi, abs(pi-PI)/PI*10000))