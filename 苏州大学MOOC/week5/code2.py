# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 16:42:48 2021

@author: 23820
"""

def is_prime(n):
    if n >= 2:
        for i in range(2,n):
            if n%i == 0:
                return False
    else:
        return False
    return True

def glodbach(n):
    if n < 2 or n%2 == 1:
        print(n, "不是一个大于2的偶数")
        return
    for p in range(2,n):
        if is_prime(p) and is_prime(n-p):
            print(n, '=', p, '+', n-p)
            return
    print('哥德巴赫猜想好像有点问题！')

def test_glodbach():
    n = int(input('请输入一个大于2的偶数，或者输入0退出：'))
    while n!=0:
        glodbach(n)
        n = int(input('请输入一个大于2的偶数，或者输入0退出：'))

test_glodbach()