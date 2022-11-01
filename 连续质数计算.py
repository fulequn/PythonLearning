# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 10:14:05 2019

@author: 23820
"""
def prime(m):
    for i in range(2, int(m**0.5)+1):
        if m%i == 0:
            return False
    return True

n = eval(input())
if n != int(n):
    m = int(n) + 1
else:
    m = int(n) 

count=0
list=[]
while count<5:
    if prime(m):
        list.append(m)
        count=count+1
        if count==5:
            print(m, end='')
        else:
            print(str(m)+",",end='')
    m=m+1

