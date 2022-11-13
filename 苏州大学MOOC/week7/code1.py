# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 22:10:27 2021

@author: 23820
"""

num1, num2=map(int, input("请输入两个整数：").split())
try:
    print("商为:%d"%(num1//num2))
    print("余数为:%d"%(num1%num2))
except ZeroDivisionError:
    print("除数为0")
