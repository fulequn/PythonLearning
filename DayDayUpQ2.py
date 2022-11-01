# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 20:35:02 2019

@author: 23820
"""
#DayDayUpQ2.py
dayfactor = 0.005
dayup = pow(1+dayfactor, 365)
daydown = pow(1-dayfactor, 365)
print("向上：{:.2f}，向下：{:.2f}".format(dayup, daydown))
