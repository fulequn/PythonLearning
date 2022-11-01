# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 16:21:44 2019

@author: 23820
"""
import requests
r=requests.get("http://www.baidu.com")
print(r.status_code)
print(r.text)
print(r.encoding)
print(r.apparent_encoding)
r.encoding="utf-8"
print(r.text)