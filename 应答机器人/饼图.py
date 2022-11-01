# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 20:14:36 2020

@author: 23820
"""

from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

# 省（自治区、直辖市），2524；
# 部委，880；
# 单位内部，761；
# 国家，2660；
# 军队系统，69；
# 其他，806
keys=['部委', '省（自治区、直辖市）', '单位内部', '国家', '军队系统', '其他']
values=[880, 2524, 761, 2660, 69, 806]


c = (
    Pie()
    .add("", [list(z) for z in zip(keys, values)])
    .set_colors(["blue", "green", "#00F5FF", "red", "#9400D3", "orange"])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="博士后科研人员参与项目级别情况",
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
    .render("pie_set_color.html")
)