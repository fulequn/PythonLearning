# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 10:24:32 2019

@author: 23820

英文字符的鲁棒输入
描述
获得用户的任何可能输入，将其中的英文字符进行打印输出，程序不出现错误。

采用遍历字符的方式实现，通过约束字母表达到鲁棒效果。
"""
#英文字符的鲁棒输入V2.py
alpha = []
for i in range(26):
    alpha.append(chr(ord('a') + i))
    alpha.append(chr(ord('A') + i))
s = input()
for c in s:
    if c in alpha:
        print(c, end="")


