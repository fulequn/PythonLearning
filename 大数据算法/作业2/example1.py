# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 19:45:53 2021

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

if __name__ == '__main__':
    print('--------AND--------')
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = AND(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))
    print('--------OR--------')
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = OR(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))
    print('--------NOT--------')
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y1 = NOT(xs[0])
        y2 = NOT(xs[1])
        print(str(xs) + " -> (" + str(y1)+', '+str(y2)+')')
    print('--------ANDNOT--------')
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = ANDNOT(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))