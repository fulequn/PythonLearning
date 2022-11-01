# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 11:35:34 2019

@author: 23820
"""
import requests 
keyword="Python"
try:
    kv={'wd':keyword}
    r=requests.get("http://www.baidu.com/s",params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
    #print(r.text)
except:
    print("爬取失败")