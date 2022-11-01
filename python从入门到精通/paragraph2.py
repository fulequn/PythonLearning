# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 10:13:52 2020

@author: 23820
"""
print("Hello Python world!")

message = "Hello Python world!"
print(message)

#修改字符串的大小写
name = 'ada loveIace'
print(name.title())
#合并字符串
first_name = 'ada'
last_name = 'lovelace'
fullname = first_name + ' ' + last_name
print(fullname) 

#使用制表符添加空白
print('Languages:\n\tPython\n\tC\n\tJavaScript')

#删除空白,；需要重新赋值
favorite_language = ' python '
print(favorite_language.rstrip())#去右空格
print(favorite_language.lstrip())#左
print(favorite_language.strip())#两端

#str()转化为字符string类型
age = 23
message = "happy "+str(age)+"rd Birthday!"
print(message)

#python之禅
import this
