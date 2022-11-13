# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 16:16:24 2021

@author: 23820
"""

import re

pa = re.compile('188\d{8}')
res = pa.findall('')
print(res)