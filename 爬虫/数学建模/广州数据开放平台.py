# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 09:31:12 2020

@author: 23820
"""
#对广州市政府数据统一开放平台数据的爬取
# import requests

# headers = {
#         'Host': 'data.gz.gov.cn',
#         'Referer': 'https://data.gz.gov.cn/odweb/catalog/catalogDetail.htm?cata_id=98381#',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
#         }
# login_url = 'https://data.gz.gov.cn/odweb/catalog/catalogDetail.htm?cata_id=98381#'
# post_url = 'https://data.gz.gov.cn/dataanaly/data/CatalogDetail.do?method=GetDataListForGrid'
# session = requests.Session()
# post_data = {
#         'cata_id': 98381,
#         'conf_type': 2,
#         'where': [],
#         '_search': 'false',
#         'rows': 10,
#         'page': 1,
#         'sidx': '',
#         'sord': 'asc',
#         }
# response = session.post(post_url, data=post_data, headers=headers)       
# print(response.status_code)
# print(response.text)


import requests
import json
import time
 

class DataOfGov(object):
    def __init__(self):
        self.headers = {
        'Host': 'data.gz.gov.cn',
        'Referer': 'https://data.gz.gov.cn/odweb/catalog/catalogDetail.htm?cata_id=98381#',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        }
        self.login_url = 'https://data.gz.gov.cn/odweb/catalog/catalogDetail.htm?cata_id=98381#'
        self.post_url = 'https://data.gz.gov.cn/dataanaly/data/CatalogDetail.do?method=GetDataListForGrid'
        self.session = requests.Session()

 
    def login(self,cata_id,page):
        post_data = {
        'cata_id': cata_id,
        'conf_type': 2,
        'where': [],
        '_search': 'false',
        'rows': 10,
        'page': page,
        'sidx': '',
        'sord': 'asc',
        }
        response = self.session.post(self.post_url, data=post_data, headers=self.headers)       
        print(page)
        print(response.status_code)
        
        for datas in self.json_text(response.text):
            self.save(datas)
    
    def json_text(self,text):
        js=json.loads(text)      
        for rows in js['rows']:
            valuelist=[]
            for key,value in rows.items():
                print(value,end='$')
                valuelist.append(value)
            print('')
            yield(valuelist)
            
    def save(self,datas):
        path=r'D:\LOG\govofdata.txt'    
        with open(path,'a') as f:
            for data in datas:
                f.write(data)
                f.write('$')
            f.write('\n')
            f.close()

if __name__ == "__main__":
    starttime=time.time()
    cata_id=98381
    main = DataOfGov()
    titlelist=['名称','地址','总泊位','经营单位','类型','地区分类','收费标准','更新时间']       
    main.save(titlelist)
    for page in range(1,307):
        login=main.login(cata_id,page)
    endtime=time.time()
    print('total time:',endtime-starttime)

    



