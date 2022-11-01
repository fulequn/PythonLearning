# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:19:38 2019

@author: 23820

爬取bilibli网站的图片
"""
'''
import requests 
import os 
import re
#url="https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/get_dynamic_detail?rid=38284175&type=2"
#url="https://i0.hdslb.com/bfs/album/b0792b70b32f6d3c1e4c6f74deafd919ce9b99fb.jpg"
url="https:\\/\\/i0.hdslb.com\\/bfs\\/album\\/b0792b70b32f6d3c1e4c6f74deafd919ce9b99fb.jpg"
root="D://pics//"
path=root+url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r=requests.get(url)
        r.encoding = r.apparent_encoding
        print(r.text)
        #imageurl = re.findall("https:(.*?).jpg")
        #for value in imageurl:
        #    image = value
        #image = "https:\/\/i0.hdslb.com\/bfs\/face\/6d10e8eba995c70a8c2d6e4a875ce8eb5e0bf460.jpg"
        with open(path,'wb')as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")'''
import requests
import os
import re#正则表达式
import json#json库
from tqdm import tqdm#进度条库
url="https://h.bilibili.com/37788889"
praseUrl="https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/get_dynamic_detail?rid={rid}&type=2"
praseUrl=praseUrl.replace('{rid}',re.findall('(\d{6,})',url)[0])
print(praseUrl)
root="image/"
try:
    try :
        html = requests.get(praseUrl).content.decode()#尝试解码
    except Exception :
        print('编码错误,切换编码!')
        html = requests.get(praseUrl).content.decode('gbk')
    js = json.loads(html)#解析html内容
    js = json.loads("{"+js['data']['card']['card'][1:-2]+"}")
    print('正在下载')
    for image in tqdm(js['item']['pictures']):#进度条
        try:
            urlimage=image['img_src']
            path = root + urlimage.split('/')[-1]
            if not os.path.exists(root):
                os.mkdir(root)
            if not os.path.exists(path):
                r=requests.get(urlimage)
                with open(path,'wb')as f:
                    f.write(r.content)
                    f.close()
            else:
                print("文件已存在")
        except:
            print("保存错误")
except:
    print("爬取失败")
print("文件保存成功")
