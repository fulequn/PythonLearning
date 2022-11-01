# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 20:10:45 2020

@author: 23820
"""
#decorated_class.py

def abc(myclass):#定义类装饰器
    class InnerClass:#定义内嵌类
        def __init__(self, z=0):
            self.z = 0
            self.wrapper = myclass()#实例化被装饰的类
            
        def position(self):
            self.wrapper.position()
            print('z axis:', self.z)
            
    return InnerClass#返回新定义的类

@abc
class coordination:
                
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def position(self):
        print('x axis:', self.x)
        print('y axis:', self.y)

if __name__ == '__main__':
    coor = coordination()#实例化被装饰的类
    coor.position()
