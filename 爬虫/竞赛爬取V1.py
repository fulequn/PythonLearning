# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 10:13:53 2019

@author: 23820
"""
import requests
from bs4 import BeautifulSoup
import threading
import numpy
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
'''
target1 = 'https://www.cust.edu.cn/lgxw/'#爬取网站

target2 = '.htm'#网页后缀

data = {
        'articleID': '40668'#文章编号
    }
# 22381


file = open('title.csv', 'a+', newline='', encoding='GBK', errors='ignore')#打开文件

for x in range(40668,61337):#遍历
    target = target1+data['articleID']+target2#获得需要爬取的网页地址
    try:
        req = requests.get(url=target, params=data, timeout = (5,5.5))#获取网页资源
    except Exception as e:#处理异常
        pass

    if(req.status_code==200):#如果访问成功

        html = req.text#网页返回的信息

        soup = BeautifulSoup(html)#解析数据

        div = soup.find_all('div', class_='articleTitle02')

        result = div[0].text.replace('<div class="articleTitle02">\n<h3>', '')

        result = result.replace('</h3>\n</div>', '')

        result = result.replace('\n', '')

        file.write(result + '\n')

        print('\r存入序号为'+data['articleID']+'条',end="")#进度条显示

    data['articleID'] = str(eval(data['articleID'])+1)#向下爬取


file.close()
'''
f = open('title.csv', 'r', newline='', encoding='GBK', errors='ignore')#打开文件
pan = pd.read_csv('title.csv', 'GBK')
pan.describe()
#承载数据的列表
one = []
two = []
three = []
special = []

for i in f:
    #print(i)
    #if i.find('赛'or'奖'):
    if '特等奖'in i :
        special.append(i)
        #print(i,end='')
    if '一等奖'in i :
        #print(i,end='')
        one.append(i)
    if '二等奖'in i:
        #print(i,end='')
        two.append(i)
    if '三等奖'in i:
        #print(i,end='')
        three.append(i)
    '''
    if '赛' in i or '奖' in i :
       print(i,end='')
       pass
    '''
#获得数据
count0=len(special)
count1=len(one)
count2=len(two)
count3=len(three)

#获得数据
count = []
count.append(count0)
count.append(count1)
count.append(count2)
count.append(count3)

data = numpy.array(count)
fig=plt.figure()    #创建一个新figure
#饼图
#解决汉字乱码
mpl.rcParams['font.sans-serif']=['SimHei']  #使用指定的汉字字体类型（此处为黑体）
labels=['特等奖','一等奖','二等奖','三等奖']#标签
colors=['yellow','green','red','blue']#颜色设置
#生成对应的饼图，将详细信息显示出来
plt.pie(count,labels=labels,colors=colors,startangle=180,shadow=True,
        explode = [0.1, 0.1, 0.1, 0.1],autopct='%1.2f%%')

plt.title("长春理工大学奖项获得情况")#设置标题
plt.show()
