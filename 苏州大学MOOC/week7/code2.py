# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 22:17:26 2021

@author: 23820
"""
#利用异常保证用户输入整数
def get_age():
    while True:
        try:
            num = int(input("你几岁？"))
            return num
        except ValueError:
            print("请输入一个整数")

#利用异常保证用户输入值域合法
def get_age():
    while True:
        try:
            num = int(input("请输入您的年龄(18-60)"))
            if num<18 or num>60:
                raise -1
            else:
                return num
        except ValueError:
            print("请输入一个整数！")
        except int:
            print('您的输入不合法！')

