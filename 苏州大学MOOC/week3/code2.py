# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 15:32:44 2021

@author: 23820
"""

mon_days = [31,28,31,30,31,30,31,31,30,31,30,31]
y=2019
m=7
d=17

sum_days=0
for i in range(1900, y):
    if (i%4==0 and i%100!=0) or i%400==0:
        sum_days += 366
    else:
        sum_days += 365
for i in range(1, m):
    if i!= 2:
        sum_days+=mon_days[i-1]
    else:
        if (y%4==0 and y%100!=0) or y%400==0:
            sum_days = sum_days+mon_days[i-1]+1
        else:
            sum_days = sum_days+mon_days[i-1]
sum_days+=d
week_day = 1+(sum_days-1)%7
print('%d-%d-%d是星期%d' %(y,m,d,week_day))