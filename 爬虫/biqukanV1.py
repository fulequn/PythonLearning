# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:11:44 2019

@author: 23820
"""
#biqukanV1.py
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # https://wenku.baidu.com/view/9d99388277c66137ee06eff9aef8941ea76e4ba6.html
    target = 'https://wenku.baidu.com/view/9d99388277c66137ee06eff9aef8941ea76e4ba6.html'
    # target='https://www.biqukan.com/2_2714/1051105.html'
    req = requests.get(url=target)
    req.encoding=req.apparent_encoding
    html = req.text
    beautifulsoup = BeautifulSoup(html, "html5lib")
    # print(beautifulsoup)
    texts = beautifulsoup.find_all('div', class_ = 'reader-container') 
    # texts = beautifulsoup.find_all('div', class_ = 'showtxt') 
    print(texts)
    #print(req.text)
    #print(beautifulsoup)


