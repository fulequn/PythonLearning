# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 10:02:15 2019

@author: 23820
"""

import random

def genpwd(length):
    i = random.randint(10**(length-1),10**length)
    if(i==10**length):
        genpwd(length)
    else:
        return i
'''
length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))
    
    import random

def genpwd(length):
    a = pow(10, length - 1)  # 定义一个下限
    b = pow(10, length) - 1  # 定义一个上限
    return "{}".format(random.randint(a, b))
length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))


# 这是自己一开始的错误答案（语文的理解博大精深T_T）
import random

def genpwd(length):
    ls = []
    for i in range(length):
        ls.append(str(random.randint(0, 9)))
    s = ''.join(ls)
    return s

length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))
'''
