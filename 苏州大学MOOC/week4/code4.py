# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 16:29:32 2021

@author: 23820
"""

L = [('摩洛哥',2,2,0,1),
     ('葡萄牙',5,4,1,5),
     ('西班牙',6,5,1,5),
     ('伊朗',2,2,0,4)]
L=sorted(L, key=lambda t:t[1], reverse=True)
L=sorted(L, key=lambda t:t[3], reverse=True)
L=sorted(L, key=lambda t:t[4], reverse=True)