# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 17:53:29 2020

@author: 23820
"""
#数学建模论文下载
import requests
from bs4 import BeautifulSoup
import os 


def download(url):
    html = requests.get(url)
    html.encoding = html.apparent_encoding
    beautifulsoup = BeautifulSoup(html.text)
    span_need = beautifulsoup.find('span', style='font-size: 16px;')
    try:
        a_need = span_need.find('a')
        newurl = a_need['href']
        root ="D://pics//"
        path = root + newurl.split('/')[-1]
        try:
            if not os.path.exists(root):
                os.mkdir(root)
            if not os.path.exists(path):
                r = requests.get(newurl)
                with open(path,'wb')as f:
                    f.write(r.content)
                    f.close()
                    print("文件保存成功")
            else:
                print("文件已存在")
        except:
            print("爬取失败")
    except :
        pass
    #print(a_need['href'])
    
if __name__ == '__main__':
    #for i in range(100):
    url = "http://special.univs.cn/service/jianmo/2018jslw/201811011186657.shtml"
    download(url)