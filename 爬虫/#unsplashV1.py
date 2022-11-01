# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:35:54 2019

@author: 23820
"""
#unsplashV1.py
import requests
from bs4 import BeautifulSoup
import os
import re#正则表达式


def printPicture(path, src):
    try:
        if not os.path.exists(path):
            os.mkdir(path)
        if os.path.exists(path):
            r=requests.get(src)
            with open(path,'wb')as f:
                f.write(r.content)
                f.close()
    except:
            print("保存错误")

if __name__ == '__main__':
    target='https://unsplash.com/photos/BIufEmUshec'
    path = 'D:\\pics'
    req = requests.get(url=target)
    req.encoding=req.apparent_encoding
    html = req.text
    beautifulsoup = BeautifulSoup(html, "html5lib")
    div = beautifulsoup.find_all('div', class_ = '_2yFK- IEpfq') 
    img = div[0].find_all('img')
    src = img[0].get('src')
    #print(html)
    #print(beautifulsoup)
    print(src)
    printPicture(path, src)

