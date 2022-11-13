# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 16:32:22 2021

@author: 23820
"""

def binary_search(L, t, low, high):
    while low<=high:
        mid=(low+high)//2
        if L[mid]==t:
            return True
        elif L[mid]<t:
            low=mid+1
        else:
            high=mid-1
    return False

L = [4, 5, 8, 9, 14, 16, 33, 35, 41]
print(binary_search(L, 16, 0, len(L)-1))
print(binary_search(L, 17, 0, len(L)-1))