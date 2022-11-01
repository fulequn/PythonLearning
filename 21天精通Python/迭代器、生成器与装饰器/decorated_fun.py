# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 20:05:47 2020

@author: 23820
"""
#decorated_fun.py

def abc(fun):#定义一个装饰器abc
    def wrapper(*args, **kwargs):#定义包装类函数
        print('开始运行……')
        fun(*args, **kwargs)#调用被装饰的函数
        print('运行结束')
    return wrapper

@abc#装饰函数语句
def demo_decoration(x):#定义普通函数，被装饰器修饰
    a = []
    for i in range(x):
        a.append(i)
    print(a)
    
@abc
def hello(name):
    print("Hello ", name)
    
if __name__ == "__main__":
    demo_decoration(5)
    print()
    hello('John')
        
    
