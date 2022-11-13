# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 21:13:58 2021

@author: 23820
"""
def base64Encode(string):
    oldBin=''
    tempStr=[]
    result=''
    base64_list='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    
    for ch in string:
        oldBin += '{:08}'.format(int(str(bin(ord(ch))).replace('0b','')))
    #得到2进制值的字符串流
    for i in range(0, len(oldBin), 6):
        tempStr.append('{:<06}'.format(oldBin[i:i+6]))
    #通过切片把每6位一合并得到的字符串放到列表中
    for item in tempStr:
        result += base64_list[int(item, 2)]
    #字符串转数字后查表，得到编码结果字符
    if len(result)%4 == 2:
        result += "=="
    elif len(result)%4 == 3:
        result += "="
    return result
