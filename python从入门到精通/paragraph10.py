# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 15:56:17 2020

@author: 23820
"""
'''
文件和异常
'''
#从文件中读取数据
#读取整个文件
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
#文件路径
#逐行读取
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())#消除多余的空白行

#创建一个包含文件各行信息的列表
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

#使用文件中的内容，处理已经读取到内存中的数据
filename='pi_30_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
#包含一百万位的大型文件

#写入文件
#写入空文件
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write('I love programming. ')

#写入多行
#python不会再写入的文本末尾自动换行，需要手动添加换行符\n

#附加到文件
with open(filename, 'a') as file_object:
    file_object.write('I also love finding meaning in large datasets.\n')
    file_object.write('I love creating apps that can run in a browser.\n')


#异常
#处理ZeroDivisionError异常
#使用try-except代码块
try:
    print(5/0)
except ZeroDivisionError:
    print('You can\'t divide by zero!')

#使用异常避免崩溃
#else代码块
first_number = input('\nFirst number: ')
second_number = input('Second number: ')
try:
    answer = int(first_number)/int(second_number)
except ZeroDivisionError:
    print('You can\'t divide by 0. ')
else:
    print(answer)

#处理FileNotFoundError
#分析文本
#使用多个文件，也就是将业务逻辑抽象为函数，再对多个文件执行
#失败时一声不吭，根据情况制定

#决定报告那些错误
    
#存储数据，json
#使用json.dump()和json.load()
    
import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)

#保存和读取用户生成的数据
import json

#如果以前存储了用户名，就加载它
#否则，就提示用户输入用户名并存储它
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input('What\'s your name?')
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We\'ll remember you when you come back , "+username+"! ")
else:
    print("Welcome back, "+username+"! ")
    
#重构
#代码能够运行，但可以做进一步的改进——将代码划分为一系列完成具体工作的函数


    