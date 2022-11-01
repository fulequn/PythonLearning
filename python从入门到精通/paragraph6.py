# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 20:03:34 2020

@author: 23820
"""
'''
字典
'''
#一个简单的字典
alien_0 = {'color':'green' ,'points':'5'}
print(alien_0['color'])
print(alien_0['points'])
#使用字典
#访问字典的值
alien_0['color']

#添加键值对
#与添加顺序可能不同，python不关心键值对的添加顺序，只关心键和值之间的关联关系
alien_0['x_position']=0

#创建空字典
alien = {}
#修改字典中的值
alien_0['color'] = 'red'

#删除键值对,消除的键值对永远消失了
del alien_0['points']

#由类似对象组成的字典
favorite_languages = {
        'jen':'python',
        'sarah':'c',
        'edward':'ruby',
        'phil':'python',
        }

#遍历字典
for key, value in favorite_languages.items():
    print('key:'+key)
    print('value:'+value)
#遍历所有的键
#for name in favorite_languages:也可以，因为遍历字典默认遍历所有键
for name in favorite_languages.keys():
    print(name.title())
#keys方法返回一个列表，包含了字典的所有键

#按顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
    print(name.title())

#遍历字典中的所有值
for language in favorite_languages.values():
    print(language.title())
    
#嵌套
#字典列表
alien_0 = {'color':'green' ,'points':5}
alien_1 = {'color':'yellow' ,'points':10}
alien_2 = {'color':'red' ,'points':15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

#在字典中存储列表
pizza = {
    'crust':'thick',
    'toppings':['mushrooms', 'extra cheese'],
    }
#概述所点的披萨
print(pizza['crust']+str(pizza['toppings']))
#嵌套不应该有太多

#在字典中存储字典
users = {
        'aeinstein':{
            'first':'albert',
            'last':'einstein',
            'location':'princeton',
            },
        'mcurie':{
            'first':'marie',
            'last':'curie',
            'location':'paris',
            },
    }


