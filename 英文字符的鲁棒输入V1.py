# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 10:20:43 2019

@author: 23820

英文字符的鲁棒输入
描述
获得用户的任何可能输入，将其中的英文字符进行打印输出，程序不出现错误。
"""
#英文字符的鲁棒输入V1.py
words = input()
for w in words:
    if (w>='a' and w<='z') or (w>='A' and w<='Z'):
        print(w,end='')