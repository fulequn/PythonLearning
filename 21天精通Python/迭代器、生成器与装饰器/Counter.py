# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 19:43:14 2020

@author: 23820
"""
#Counter.py

class Counter:#定义用于计数的类
    
    def __init__(self, x=0):    #定义构造方法，初始化实例属性x
        self.x = x
        
counter = Counter()#实例化类Counter

def used_iter():
    counter.x += 2#修改实例属性的值
    return counter.x

for i in iter(used_iter, 8):
    print('本次遍历的数值', i)
    