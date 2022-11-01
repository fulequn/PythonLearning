# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 16:47:15 2021

@author: 23820
"""


import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

#与非门
def ANDNOT(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 1
    else:
        return 0

#非门
def NOT(x1):
    if x1 == 0:
        return 1
    else:
        return 0

#或门
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.3#只需要让0,0不符合即可
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
#异或门
def XOR(x1, x2):
    #或门，第1层
    or1 = OR(x1, x2)
    #与非门，第1层
    andnot1 = ANDNOT(x1, x2)
    #与门，第2层
    and2 = AND(or1, andnot1)
    return and2

if __name__ == '__main__':
    print('--------XOR--------')
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = XOR(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))
