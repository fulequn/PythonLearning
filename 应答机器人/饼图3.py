# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 20:38:58 2020

@author: 23820
"""

# 博士后科研人员获基金资助情况：
# 博士后科学基金，1324；
# 社会科学基金，169；
# 自然科学基金，891；
# 其它，309

# 博士后科研人员论文收录情况：
# A&HCI 5;
# CSSCI,2042;
# CSCD,468;
# CSCI,9;
# EI,1269;
# CPCI,75;
# CSTPCD,42;
# SCI,6138;
# SSCI,107;
# 其他，2013

# 博士后科研人员授权专利情况：
# 外观设计，10；
# 发明专利，1239；
# 其它，34；
# 实用新型，347；


from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

# keys=['博士后科学基金', '社会科学基金', '自然科学基金', '其他']
# values=[1324, 169, 891, 309]

#博士后科研人员论文收录情况
# keys=['A&HCI', 'CSSCI', 'CSCD', 'CSCI', 'EI', 'CPCI', 'CSTPCD',
#       'SCI', 'SSCI', '其他']
# values=[5,2042,468,9,1269,75,42,6138,107,2013]

# 博士后科研人员授权专利情况
keys=['外观设计', '发明专利', '其它', '实用新型']
values=[10,1239, 34, 347]


c = (
    Pie()
    .add("", [list(z) for z in zip(keys, values)])
    # .set_colors(["#4F81BD", "#C0504D", "#9BBB59", "#8064A2"])
    # .set_colors(["#4572A7", "#AA4643", "#89A54E", "#71588F", 
    #              '#4198AF', '#DB843D', '#93A9CF', '#D19392',
    #              '#B9CD96', '#A99BBD'])
    .set_colors(["#8064A2", "#4F81BD", "#C0504D", "#9BBB59"])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            # title="博士后科研人员获基金资助情况",
            # title="博士后科研人员论文收录情况",
            title="博士后科研人员授权专利情况",
            pos_left="center",
            pos_top='top',
            title_textstyle_opts=opts.TextStyleOpts(font_size=30)         
            ),
        legend_opts=opts.LegendOpts(
            type_="scroll", 
            pos_left="81%", 
            pos_top="20%",
            orient="vertical",
            textstyle_opts=opts.TextStyleOpts(font_size=16) 
            ),
        )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    # .render("bingtu2.html")
    # .render("博士后科研人员论文收录情况.html")
    .render("博士后科研人员授权专利情况.html")
)