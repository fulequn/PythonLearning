# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 20:56:45 2019

@author: 23820

获得输入的一个字符串s，以字符减号(-)分割s，将其中首尾两段用加号(+)组合后输出。
"""
s = input()
ls = s.split('-')
print(ls[0] + "+" + ls[-1])