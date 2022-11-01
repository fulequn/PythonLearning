# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 10:52:41 2020

@author: 23820
"""

'''
操作列表
'''
#列表的遍历
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

#在for循环中添加操作
for magician in magicians:
    print(magician.title() + ',that was a great trick!')
print('thank you, every one, That was a great magic show!')
#range的使用
for value in range(1,5):
    print(value)
numbers = list(range(2,11,2))

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

#对数字列表进行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(max(digits))
print(min(digits))
print(sum(digits))

#列表解析
squares = [value**2 for value in range(1, 11)]
print(squares)

#使用列表的一部分
#切片
players = ['charles', 'maryina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:4])
print(players[-3:])

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

#元组
#定义元组,元素不可被修改
dimensions = (200, 50)
print(dimensions[0])
for item in dimensions:
    print(item)

#修改元组变量,给变量赋值是合法的
dimensions = (200, 50)
dimensions = (400, 100)

