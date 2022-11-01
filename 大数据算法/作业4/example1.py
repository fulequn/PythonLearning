# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 16:22:20 2021

@author: 23820
"""

import numpy as np
import pandas as pd

def draw (ty):
    inputs = np.random.uniform (-5, 5, 50)
    inputs.sort()
    if ty == 'sigmoid':    
        outputs = sigmoid(inputs)
    elif ty == 'tanh':
        outputs = tanh(inputs)
    elif ty == 'relu':
        outputs = relu(inputs)
    elif ty == 'sgn' :
        outputs = sgn(inputs.copy())
    else :
        outputs = piecewise (inputs.copy())
    df = pd.DataFrame(np.vstack((inputs, outputs))).T.rename(columns={0:'input',1:'output'})
    df.plot()
    return 
    
def sgn (x):
    mask = x>0
    x[mask] = 1
    mask = x==0
    x[mask] = 0
    mask = x<0
    x[mask] = -1
    return x
    
def piecewise (x):
    mask = x<-1
    x[mask] = -1
    mask = x>1
    x[mask] = 1
    return x

def tanh (x):
    return (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))

def sigmoid (x):
    return 1.0/(1+np.exp(-x))

def relu (x):
    return np.maximum(x, 0)

s = input ()
draw (str(s))

