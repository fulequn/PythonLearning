# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 10:29:28 2021

@author: 23820
"""

tz=float(input('体重(kg)='))
sg=float(input('身高(m)='))

bmi = tz/sg/sg
print('BMI = %.1f' % bmi)

s = "体重偏轻" if bmi<18.5 else '正常' if bmi<23.0 else '超重' if bmi<25.0 else \
    '轻度肥胖' if bmi<29.0 else '肥胖'
print(s)