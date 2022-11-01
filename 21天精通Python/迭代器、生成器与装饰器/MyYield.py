# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 19:47:36 2020

@author: 23820
"""
#MyYield.py

def MyYield(n):#定义一个生成器
    while n > 0:
        print("开始生成……")
        yield n
        print('完成一次')
        n -= 1
        
if __name__ == "__main__": 
    for i in MyYield(4):
        print("遍历得到值", i)
    print()
    my_yield = MyYield(3)#生成一个生成对象
    print("已经实例化生成器对象")
    my_yield.__next__()#手工调用其特殊方法，获取序列中一个值
    print("第二次调用__next__()方法：")
    my_yield.__next__()
