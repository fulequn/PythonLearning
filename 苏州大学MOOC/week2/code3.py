# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 10:38:50 2021

@author: 23820
"""
date = input('日期=')
leap = False
legal = False

month1 = {1, 3, 5, 7, 8, 10, 12}
month2 = {4, 6, 9, 11}

year,month,day = (int(x) for x in tuple(date.split("-")))

if year%4==0 and year%100!=0 or year%400==0:
    leap = True
if month in month1:
    if 1<=day<=31:
        legal = True
elif month in month2:
    if 1<=day<=30:
        legal=True
elif month == 2:
    if not leap and 1<=day<=28:
        legal=True
    elif leap and 1<=day<=29:
        legal=True

print("%d年%d月%d日是%s" % (year, month, day, "合法日期"if legal else "不合法日期"))
        
