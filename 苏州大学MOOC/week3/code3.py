# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 15:51:59 2021

@author: 23820
"""

for cock in range(0, 21):
    for hen in range(0, 34):
        chick = 100-cock-hen
        if cock*5+hen*3+chick//3==100 and chick%3==0:
            print("公鸡{0:2d} 母鸡{1:2d} 小鸡{2:2d}".format(cock, 
                                                      hen, chick))