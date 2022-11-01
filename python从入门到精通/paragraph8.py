# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 09:12:17 2020

@author: 23820
"""
'''
函数
'''
def greet_user():
    '''
    这是文档字符串
    显示简单的问候语
    '''
    print('Hello!')

greet_user()

#向函数传递信息
def greet_user(username):
    '''
    这是文档字符串
    显示简单的问候语
    '''
    print('Hello!'+username.title())

#实参和形参
    
#传递实参
#位置实参，基于实参的顺序
def describe_pet(animal_type, pet_name):
    '''
    显示宠物的信息
    '''
    print('\nI have a '+animal_type+'.')
    print('My' + animal_type +"'s name is "+ pet_name.title()+'.')

describe_pet('hamster', 'harry')

#调用函数多次
#位置实参的顺序很重要

#关键字参数，传递给函数的名称-值对
describe_pet(animal_type = 'hamster', pet_name = 'harry')

#默认值，放在后面
#def describe_pet(pet_name, animal_type='dog'):

#等效的函数调用

#避免实参错误

#返回值
#返回简单值
def get_formatted_name(first_name, last_name):
    '''
    返回整洁的姓名
    '''
    full_name = first_name + ' ' +last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#让实参变成可选的
def get_formatted_name(first_name, last_name, middle_name=''):
    '''
    返回整洁的姓名
    '''
    if middle_name:#不为空字符
        full_name = first_name + ' '+middle_name+' '+last_name
    else:
        full_name = first_name + ' ' +last_name
    return full_name.title()

#返回字典
#结合使用函数和while循环
#传递列表，实参可以是列表
#在函数中可以修改列表，都是永久性的，可以提高工作效率

def print_models(unprinted_designs, completed_models):
    '''
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models
    '''
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        #模拟根据设计制作3D打印模型的过程
        print('Printing model: '+ current_design)
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    '''
    显示打印好的所有模型
    '''
    print('\nThe following models have been printed. ')
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
#禁止函数修改列表，传递副本
#function_name(list_name[:])
#除了有充分的理由，否则不要这样做，副本会引起开销

#传递任意数量的实参
def make_pizza(*toppings):
    '''
    打印顾客点的所有配料
    '''
    print(toppings)
#结合使用位置实参和任意数量实参
#使用任意数量的关键字实参
    
#将函数存储在模块里
#导入整个模块
#导入特定函数
#使用as给函数指定别名
#使用as给模块指定别名
#导入模块中的所有函数，不推荐

