
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 15:38:37 2020

@author: 23820
"""
n = int(input())
if n < 1:
    exit()
elif n > 2 * (10**5):
    exit()
a = list(map(int, input().split()))
if len(a) > n:
    exit()
elif len(a) < n:
    exit()
mn = min(a)
mx = max(a)
if mx > 300:
    exit()
elif mn < -300:
    exit()
def MaxSum(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return max(arr[0],0)
    data = list([])
    for k, v in enumerate(arr):
        if k == 0:
            data.append(max(v,0))
        elif k == 1:
            data.append(max(arr[0], v))
        else:
            data.append(max(data[k - 1], data[k - 2] + v))
    return data[len(arr) - 1]
print(MaxSum(a))
exit(0)

