# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 20:55:23 2021

@author: 23820
"""

import random
PI = 3.141592654

def gen_pi():
    count, max_c = 0, 10000000
    for i in range(0, max_c):
        x, y = random.random(), random.random()
        if x*x+y*y <= 1:
            count += 1
    return (count/max_c*4)

if __name__ == '__main__':
    sum_dif, k = 0, 20
    for i in range(k):
        pi = gen_pi()
        dif = abs(pi-PI)/PI*1000000
        sum_dif += dif
        print("%d\tpi=%.7f误差率(*10000=%.3f)" % (i+1, pi, abs(pi -PI)/PI*10000))
    print('平均误差率(*10000)=%.3f' % (sum_dif/k))
