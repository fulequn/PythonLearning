# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 16:38:00 2021

@author: 23820
"""

def my_bin(n):
    L = []
    if n<0:
        n *= -1
        L.append('-')
    v = 1
    while v<=n//2:
        v *= 2
    while v>0:
        if n<v:
            L.append('0')
        else:
            L.append('1')
            n -= v
        v //= 2
    return ''.join(L)