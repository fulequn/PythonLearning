# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 10:24:34 2020

@author: 23820
"""
'''
列表
'''
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

#访问列表元素
print(bicycles[0])
#索引是从0而不是1开始

#修改元素
bicycles[0] = 'ducati'

#添加元素
bicycles.append('yamaha')

#在列表中插入元素
bicycles.insert(0, 'honda')#在插入元素后面的既有的元素会右移一位

#从列表中删除元素
#del
del bicycles[0]
#pop，删除队尾元素且可以继续使用
last_bicycle = bicycles.pop()
#pop弹出任意位置处元素
first_bicycle = bicycles.pop(0)
'''
del：删除一个元素，并且不再以任何方式使用它
pop:删除元素后还能继续使用它
'''
#根据值来删除元素
bicycles.remove('cannondale')

#组织列表
#使用方法sort()进行永久排序
cars = ['bmw', 'audi', 'subaru']
cars.sort()
print(cars)
#使用sorted()进行临时排序
sorted(cars)
#反序，reverse = True
sorted(cars, reverse = True)

#反序,永久性更改，想要恢复原状，只需要再执行一次就行
cars.reverse()

#确定列表长度
len(cars)

#避免索引错误