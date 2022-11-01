# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 20:14:37 2020

@author: 23820
"""
# 博士后科研人员获基金资助情况

from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

# 博士后科学基金 1324
# 社会科学基金 169
# 自然科学基金 891
# 其他 309
keys=['博士后科学基金', '社会科学基金', '自然科学基金', '其他']
values=[1324, 169, 891, 309]


c = (
    Pie()
    .add("", [list(z) for z in zip(keys, values)])
    .set_colors(["#4F81BD", "#C0504D", "#9BBB59", "#8064A2"])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="博士后科研人员获基金资助情况",
            pos_left="center",
            pos_top='top',
            title_textstyle_opts=opts.TextStyleOpts(font_size=30)         
            ),
        legend_opts=opts.LegendOpts(
            type_="scroll", 
            pos_left="75%", 
            pos_top="20%",
            orient="vertical",
            textstyle_opts=opts.TextStyleOpts(font_size=16) 
            ),
        )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("bingtu2.html")
)