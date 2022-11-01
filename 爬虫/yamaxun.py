# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 11:25:35 2019

@author: 23820
"""
import requests
url = "https://www.amazon.cn/?_encoding=UTF8&ref_=nav_logo"
try:
    kv = {'User-Agent':'Mozilla/5.0'}
#重新定义头部信息
    r = requests.get(url, headers=kv)
    print(r.request.headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    #print(r.text)
except:
    print("抓取失败")