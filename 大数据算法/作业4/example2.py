# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 16:35:02 2021

@author: 23820
"""

import numpy as np
import pandas as pd

    
def sigmoid(x):
    return 1.0/(1+np.exp(-x))

def relu(x):
    return np.maximum(x, 0)

def step(x):
    y = x.copy()
    y[y>0]=1
    y[y==0]=1/2
    y[y<0]=0
    return y

#sigmoid
inputs = np.random.uniform (-2, 2, 400)
inputs.sort()
outputs = sigmoid(inputs)
df = pd.DataFrame(np.vstack((inputs, outputs))).T.rename(columns={0:'input',1:'output'})
df.plot()

#relu
outputs = relu(inputs)
df = pd.DataFrame(np.vstack((inputs, outputs))).T.rename(columns={0:'input',1:'output'})
df.plot()

#step function
outputs = step(inputs)
df = pd.DataFrame(np.vstack((inputs, outputs))).T.rename(columns={0:'input',1:'output'})
df.plot()