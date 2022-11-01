# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 21:45:44 2020

@author: 23820

使用龙贝格积分Romberg来计算sinx/x在0到1上的积分。
"""

import math

def fx(x):
    return math.sin(x)/x

print(fx(0.5))