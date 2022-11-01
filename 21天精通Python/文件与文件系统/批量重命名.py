# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 21:15:52 2020

@author: 23820
"""
#批量重命名.py
import os
prefix = 'Python' #重命名后的文件起始字符
length = 2#除去perfix后，文章名要达到的长度
base = 1#文件名的起始数
fileformat = 'mdb'#文件的后缀名

def padLeft(s, num, padstr):
    '''
    将文件名补全到指定长度
    s:要补全的字符，num:要达到的长度，padstr:未达到长度所添加的字符
    '''
    stringlength = len(s)
    n = num - stringlength
    if n >= 0:
        s = padstr*n + s
    return s

#为了避免误操作，这里先提示用户
print('the files in %s will be renamed' % os.getcwd())
all_files = os.listdir(os.getcwd())
print([f for f in all_files if os.path.isfile(f)])#输出当前目录下所有文件名
userinput = input('press y to continue\n')#获取用户输入
if userinput.lower() != 'y':#判断用户输入，以决定是够进行重命名操作
    exit()
filenames = os.listdir(os.curdir) #获取当前目录中的内容
#基数减1，为了下面i=i+1在第一次执行时等于基数
i = base -1
for filename in filenames: #遍历目录中的内容，进行重命名操作
    i = i+1
    #判断当前路径是否为违建，并且不是“批量重命名.py”
    if filename != "批量重命名.py" and os.path.isfile(filename):
        name = str(i) #将i转化为字符
        name = padLeft(name, length, '0') #将name补全到指定长度
        t = filename.split('.')  #分割文件名，以检查其是否是所要修改的类型
        m = len(t)
        if fileformat == '': #如果未指定文件类型，则修改当前目录中的所有文件
            os.rename(filename, prefix+name+'.'+t[m-1])
        else: #否则只修改指定类型
            if t[m-1] == fileformat:
                os.rename(filename, prefix+name+'.'+t[m-1])
            else:
                i = i-1 #保持i连续
    else:
        i = i-1 #保持i连续
all_files = os.listdir(os.getcwd())
print([f for f in all_files if os.path.isfile(f)])#输出当前目录下所有文件名


