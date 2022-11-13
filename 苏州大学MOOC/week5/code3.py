# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 20:42:51 2021

@author: 23820
"""

def factorial(n):
    if n==1:
        return 1
    else:
        return n *factorial(n)

def my_max(L):
    if len(L)==1:
        return L[0]
    else:
        return max(L[0], my_max(L[1:]))

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def good_fibonacci(n):
    if n<=1:
        return (n, 0)
    else:
        (a, b)=good_fibonacci(n-1)
        return (a+b, a)
