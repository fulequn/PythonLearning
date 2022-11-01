# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 21:14:23 2019

@author: 23820
"""
import pip 
from subprocess import call 
  
for dist in pip.get_installed_distributions(): 
    call("pip install --upgrade " + dist.project_name, shell=True) 
