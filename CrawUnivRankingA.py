# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 19:21:38 2019

@author: 23820
"""
#CrawUnivRankingA.py
import requests
from bs4 import BeautifulSoup
import bs4
 
def getHTMLText(url):         #返回网页完整信息
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
 
def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")    #解析网页信息
    for tr in soup.find('tbody').children:    #tbody的所有子节点
        if isinstance(tr, bs4.element.Tag):    #如果是Tag类型
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])         #向列表中添加元素
 
def printUnivList(ulist, num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名","学校名称","总分"))    #格式化输出
    for i in range(num):    
        u=ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2]))
     
def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    #print(html)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20) # 20 univs
main()
