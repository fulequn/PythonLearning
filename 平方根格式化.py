# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 20:55:33 2019

@author: 23820

获得用户输入的一个整数a，计算a的平方根，保留小数点后3位，并打印输出。
‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬
输出结果采用宽度30个字符、右对齐输出、多余字符采用加号(+)填充。
‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬
如果结果超过30个字符，则以结果宽度为准。
"""

a = eval(input())
val=pow(a,0.5)
print("{:+>30.3f}".format(val))