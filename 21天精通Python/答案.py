# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 15:43:13 2020

@author: 23820
"""
#! /usr/bin/env python
# _*_  coding:utf-8 _*_
# name: 智慧树网课查询程序
# 作者：TRY
# 博客：****
# QQ : *****
# 吾爱破解：[url=http://www.52pojie.cn]www.52pojie.cn[/url]
# time: 2020.02.25
import json
import requests
import urllib
from colorama import Fore, Back, Style, init
print(
    """
              $$\             $$\                       $$$$$$$$\ $$$$$$$\  $$\     $$\ 
              $$ |            $$ |                      \__$$  __|$$  __$$\ \$$\   $$  |
$$\  $$\  $$\ $$ |  $$\       $$$$$$$\  $$\   $$\          $$ |   $$ |  $$ | \$$\ $$  / 
$$ | $$ | $$ |$$ | $$  |      $$  __$$\ $$ |  $$ |         $$ |   $$$$$$$  |  \$$$$  /  
$$ | $$ | $$ |$$$$$$  /       $$ |  $$ |$$ |  $$ |         $$ |   $$  __$$<    \$$  /   
$$ | $$ | $$ |$$  _$$<        $$ |  $$ |$$ |  $$ |         $$ |   $$ |  $$ |    $$ |    
\$$$$$\$$$$  |$$ | \$$\       $$$$$$$  |\$$$$$$$ |         $$ |   $$ |  $$ |    $$ |    
 \_____\____/ \__|  \__|      \_______/  \____$$ |         \__|   \__|  \__|    \__|    
                                        $$\   $$ |                                      
                                        \$$$$$$  |                                      
                                         \______/                                       
    """)
print("===========智慧树知到网课答案查询程序============")
print("==================by:TRY=======================")
print("=================QQ:****=================")
print("============个人博客：www.nctry.com ============")
print("")
print("说明：直接输入需要查询的问题就行了")
def getanswer():
    api = 'http://tiku.xuexibao.tech/api/mobile/Index/searchQuestion'
    content = input("请输入你的问题：")
    if content == "":
        print("亲，你还没有输入你的问题勒~")
    else:
        content_url = urllib.parse.quote(content)  # 将字符进行url编码
        # print(content_url)
        headers =  {
                "Host": "tiku.xuexibao.tech",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0",
                "Accept": "*/*",
                "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                "Accept-Encoding": "gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Referer": "http://wk.tteam.tk/",
                "X-Requested-With": "XMLHttpRequest",
                "Authorization": "BearereyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vdGlrdS54dWV4aWJhby50ZWNoL2FwaS9tb2JpbGUvSW5kZXgvYXBwTG9naW4iLCJpYXQiOjE1NzU2MzA5MzAsImV4cCI6MTg5MDk5MDkzMCwibmJmIjoxNTc1NjMwOTMwLCJqdGkiOiJ2VDlYZTkxcXRZaWMwamR3Iiwib3BlbklkIjoib1JFNXIxSTVFTzZEYVAydzYwbWRXUzhlLW16ayIsIndlY2hhdF9pZCI6Im9SRTVyMUk1RU82RGFQMnc2MG1kV1M4ZS1temsiLCJ1bmlvbmlkIjoib3EySG8xVy1iN2dzaUNoLXZPRlBWVk1NalVJOCIsImdvbmd6aG9uZyI6InpodWtlYmFvIn0.ed6ZRuQ9RCXVhDfE8QJiS_Bx7b9cDqNUGYO5hFAOMfA",
                "Content-Length": "320",
                "Origin":"http://wk.tteam.tk",
            }
        data = "goods_id=28303&content="+ content_url   # 提交的数据
        down = requests.post(api,data=data,headers=headers)             #利用requests的post来进行post提交
        d = down.text
        answer = json.loads(d)           #利用json这个库来提取数据
        error = answer['error']
        if error == 0 :       #利用json这个库来判断网站是否正确。
            print("答案获取成功！")
            print('你的问题是：', answer['data'][0]['question'])
            print('这道题的答案是:', answer['data'][0]['answer'])
            print("-----------我是分割线--------------")
        else:
            print("出现了一些奇怪的问题，请重试！")
if __name__ == '__main__':
    k = 1
    while k < 100:
        getanswer()
        k += 1;
    else:
        print("不好意思，出了一点小问题。请重新尝试。")
        input("请按回车键继续。")
