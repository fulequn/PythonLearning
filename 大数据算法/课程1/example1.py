# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 18:28:13 2021

@author: 23820
"""
import matplotlib.pyplot as plt
import numpy as np
 
if __name__ == '__main__':
    x = np.linspace(-np.pi, np.pi, 256, endpoint= True)
    y = np.cos(x)
    y1 = np.sin(x)
 
    plt.plot(x,y)
    plt.plot(x,y1)
    plt.title("Functions $\sin$ and $\cos$")
 
    plt.xlim(-3.0, 3.0)
    plt.ylim(-1.0, 1.0)
 
    plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
 
    plt.yticks([-1, 0, +1],
               [r'$-1$', r'$0$', r'$+1$'])
 
    plt.show()
