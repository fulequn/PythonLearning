# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 21:41:15 2019

@author: 23820
"""
#import bs4
from bs4 import BeautifulSoup
import requests 
r= requests.get("https://python123.io/ws/demo.html")
demo =r.text
soup = BeautifulSoup(demo, 'html.parser')
print(soup.prettify())