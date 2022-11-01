# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 11:14:25 2020

@author: 23820
"""
'''
if语句
'''
cars = ['bmw', 'audi', 'subaru']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#条件测试
#检测时忽略大小写
car = 'Audi'
car.lower()=='audi'

#检测不相等
car.lower()!='audi'

#检查多个条件
age_0 = 18
age_1 = 22

age_0 >= 21 and age_1 >=21
age_0 >= 21 or age_1 >=21

#检查特定的值是否在列表中
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
#检查特定的值不在列表中
'mushrooms' not in requested_toppings

if age_0 >=18:
    print('you are old enough to vote')
#if-else语句
#if-elif-else语句
#测试多个条件就需要使用多个代码块

#使用if处理列表
#检查特定元素
for requested_topping in requested_toppings:
    if requested_topping == 'pineapple':
        
    