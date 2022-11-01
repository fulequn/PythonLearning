# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 20:43:31 2020

@author: 23820
"""

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker

years = ["{}年".format(i) for i in range(1987,2020)]
data = [6,12,7,16,11,20,20,27,33,34,33,43,74,
        62,88,100,129,156,168,116,207,114,326,457,
        456,440,447,421,400,464,302,291,332]

c = (
    Bar()
    .add_xaxis(years)
    .add_yaxis("博士生", data)
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="吉林省历年博士后研究人员招收情况"
            ),
        # datazoom_opts=opts.DataZoomOpts(),
    )
    .render("吉林省历年博士后研究人员招收情况.html")
)