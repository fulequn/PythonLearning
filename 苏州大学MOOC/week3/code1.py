# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 10:47:10 2021

@author: 23820
"""

for i in range(1, 10):
    for j in range(1, i+1):
        #print("{}*{}={}\t".format(j, i, j*i), end='')
        print("%d*%d=%d\t" % (j, i, j*i), end='')
    print()