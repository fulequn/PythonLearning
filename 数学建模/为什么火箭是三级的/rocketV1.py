# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 14:39:51 2020

@author: 23820
"""
#https://zhuanlan.zhihu.com/p/63204327
#rocketV1.py
import numpy as np

lambda_m = 0.1
v = 10.5
u = 3
for n in range(2, 10):
    mass_ratio = np.power((1-lambda_m)/(np.exp(-(v/(n*u)))-lambda_m), n)
    print("{}级火箭的质量比(初始质量/有效载荷):   {:.1f}".format(n, mass_ratio))

n = 1000
mass_ratio = np.power((1-lambda_m)/(np.exp(-(v/(n*u)))-lambda_m), n)
print("{}级火箭的质量比(初始质量/有效载荷):{:.1f}".format(n, mass_ratio))