# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 20:34:01 2020

@author: 23820
"""
'''
用户输入和while循环
'''
#input的工作原理
message = input('Tell me something, and I will repeat it back to you: ')
print(message)

#使用int来获取数值输入
age = input('How old are you? ')
print(age)
age = int(age)#此时才能进行数值运算

#求模运算符
4%3

#while循环简介
#使用while循环
current_number = 10
while current_number <= 5:
    print(current_number)
    current_number += 1

#让用户选择何时退出
message = ''
while message !='quit':
    message = input()
    if message != 'quit':
        print(message)

#使用标志，定义一个用于判断程序状态的变量
#使用break退出循环
#在循环中使用continue
#避免无限循环

#使用while循环来处理列表和字典
#首先创建一个待检验的用户列表
#和一个用于存储已验证的用的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

#验证每个用户，直到没有未检验用户为止
#将每个经过检验的列表都移到已检验用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(current_user.title())
    confirmed_users.append(current_user)

#显示所有已验证用户
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    
#删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#使用用户输入来填充字典
resposes = {}
#设置一个标志，指出调查是否继续
polling_active = True
while polling_active:
    #提示输入被调查者的名字和回答
    name = input('\nWhat is your name? ')
    respose = input('Which mountain would you like to climb someday? ')
    
    #将答卷存储在字典中
    resposes[name] = respose
    
    #看看是否还有人要参与调查
    repeat = input('Would you like to let another person respond?(yes/no) ')
    if repeat == 'no':
        polling_active = False

#调查结束，显示结果
print('\n---Poll Results---')
for name, respose in resposes.items():
    print(name + 'would like to climb'+respose)
    

