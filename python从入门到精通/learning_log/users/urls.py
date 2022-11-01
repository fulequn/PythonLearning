# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 21:43:18 2020

@author: 23820
"""
#urls.py
'''为应用程序user定义URL模式'''

from django.urls import path
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from . import views

app_name='users'#现在需要标明项目名

urlpatterns = [
    #登录界面
    path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
    
    #注销
    path('logout/', views.logout_view, name='logout'),
    
    #注册页面
    path('register/', views.register, name='register'),
    
]
