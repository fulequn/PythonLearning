# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 13:17:27 2019

@author: 23820
"""
factor = 0.01
def dayup1(factor):
    return pow(1+factor,365)
def dayup2(factor):
    sum = 1.0
    for i in range(365):
        if i%7 in [6,0]:
            sum = sum*(1-0.01)
        else:
            sum = sum*(1+factor)
    return sum
while dayup2(factor) < dayup1(0.01):
    factor += 0.001
print("工作日的努力参数是: {:.3f}".format(factor))