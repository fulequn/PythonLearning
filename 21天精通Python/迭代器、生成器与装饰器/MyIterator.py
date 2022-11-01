# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 19:35:06 2020

@author: 23820
"""
#MyIterator.py

class MyIterator:#自定义迭代器类
    
    def __init__(self, x=2, xmax=100):#定义构造方法，初始化实例属性
        self.__mul,self.__x = x,x
        self.__xmax = xmax
    
    def __iter__(self):#定义迭代器协议方法，返回类自身
        return self
    
    def __next__(self):#定义迭代器协议方法
        if self.__x and self.__x != 1:
            self.__mul *=self.__x
            if self.__mul <= self.__xmax:
                return self.__mul#返回值
            else:
                raise StopIteration#引发StopIteration错误
        else:
            raise StopIteration
            
if __name__ == '__main__':
    myiter = MyIterator()#实例化MyIterator对象
    for i in myiter:
        print('迭代的数据元素为：',i)