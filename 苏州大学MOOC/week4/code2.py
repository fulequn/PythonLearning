# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 16:18:08 2021

@author: 23820
"""

import re

telNumber=''
pa=re.compile('(\d{3,4})-(\d{7,8})')

res=pa.findall(telNumber)
print(res)

inx=0
while True:
    res=pa.search(telNumber, inx)
    if not res:
        break
    for i in range(3):
        print(res.group(i)," ",res.start(i)," ",res.end(i))
    inx = res.end(2)