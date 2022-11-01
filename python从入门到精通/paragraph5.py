# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 19:58:12 2020

@author: 23820
"""
cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

age_0 = 22
age_1 = 18
#多个条件的检查
print(age_0 >= 21 and age_1 >=21)
print(age_0 >= 21 or age_1 >= 21)
#检查特定值是否包含在列表中
requested_topping = ['mushroom', 'onions', 'pineapple']
print('mushrooms' in requested_topping)
#检查元素不在列表中
if 'pepperoni' not in requested_topping:
    print('pepperoni'.title())
    
#布尔表达式
#if语句
if age_0 >=18:
    print('you are old enough to vote')
#if-else语句
#if-elif-else语句
#测试多个条件就需要使用多个代码块

#使用if处理列表
#检查特定元素
for requested_topping in requested_toppings:
    if requested_topping == 'pineapple':
