# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:54:19 2019

@author: 23820
"""

import requests 
import os 
#url ="http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"
#url = "https://python123.io/resources/pye/hamlet.txt"
url = "https://link.springer.com/content/pdf/10.1186%2Fs13677-015-0045-5.pdf"
root ="D://pics//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb')as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")