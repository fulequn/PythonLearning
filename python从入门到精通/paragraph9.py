# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 14:51:20 2020

@author: 23820
"""
'''
类
'''
#创建和使用类
class Dog():
    '''
    一次模拟小狗的简单尝试
    '''
    
    def __init__(self, name, age):
        '''
        初始化属性name和age
        '''
        self.name = name
        self.age = age
        
    def sit(self):
        '''
        模拟小狗被命令时坐下
        '''
        print(self.name.title()+' is now sitting. ')
        
    def roll_over(self):
        '''
        模拟小狗被命令时打滚
        '''
        print(self.name.title()+'rolled over!')

#根据类创建实例
my_dog = Dog('willie', 6)
print("My dog's name is "+my_dog.name +" and it's "+my_dog.age+" years old")
#访问属性
my_dog.name
#访问方法
my_dog.sit()
#创建多个实例

#使用类和实例
#Car类
class Car():
    '''
    一次模拟汽车的尝试
    '''
    def __init__(self, make, model, year):
        '''
        初始化汽车信息
        '''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0#给属性指定默认值
    
    def get_descriptive_name(self):
        '''
        返回整洁的描述性信息
        '''
        long_name = str(self.year) + ' '+ self.make+' '+self.model
        return long_name.title()
    
    def update_odometer(self, mileage):
        '''
        将里程表读书设置为指定的值
        禁止将里程表读数往回调
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can\'t roll back an odometer. ')
            
    def increment_odometer(self, miles):
        '''
        将里程表增加指定的量
        '''
        self.odometer_reading += miles
    
    def read_odometer(self):
        '''
        打印一条指出汽车里程的信息
        '''
        print('This car has '+str(self.odometer_reading) + ' miles on it')
    
my_new_car=Car('audi', 'a4', 2016)

#修改属性的值
#直接修改属性的值
#my_new_car.odometer_reading=23
#通过方法修改,如上
#通过方法对属性的值进行递增
        

#继承(父类和子类)
#子类的方法__init__()
class ElectricCar(Car):
    '''
    电动汽车的独到之处
    '''
    
    def __init__(self, make, model, year):
        '''
        初始化父类的属性
        电动汽车的独特之处
        '''
        super().__init__(make, model, year)
        self.battery_size = 70
    
    def describe_battery(self):
        '''
        打印一条描述电瓶容量的消息
        '''
        print('This car has a '+str(self.battery_size)+"-kWh battery. ")
        
my_tesla = ElectricCar('tesla', 'model s', 2016)


print(my_tesla.get_descriptive_name())

#给子类定义属性和方法
#重写父类方法
#将实例用作属性，类中有着其他类的实例
#模拟实物

#导入类
#导入单个类
#在一个模块中存储多个类
#导入整个模块
#导入模块中的所有类
#在一个模块中导入另一个模块
#自定义工作流程
from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages['jen']='python'
favorite_languages['sarsh']='c'
favorite_languages['edward']='ruby'
favorite_languages['phil']='python'

for name, language in favorite_languages.items():
    print(name+'  '+language)
#类编码风格
