# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 19:27:52 2019

@author: 23820
"""
#CrawUnivRankingB.py
import requests
from bs4 import BeautifulSoup
import bs4
 
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
 
def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")     #解析网页信息
    for tr in soup.find('tbody').children:    #tbody的所有子节点
        if isinstance(tr, bs4.element.Tag):    #如果是Tag类型
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])
 
def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"    #模板字符串
    print(tplt.format("排名","学校名称","总分",chr(12288)))    #chr(12288)是中文里的空格
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))
     
def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20) # 20 univs
main()
