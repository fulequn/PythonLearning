# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 20:19:53 2019

@author: 23820
"""
def ss(i):
    x=int(i)
    for m in range(2,x-1):
        if(x%m==0):
            return False
    return True
sum = 0
for i in range(2,101):
    if ss(i):
        sum+=i
        #print(i)
print(sum)
