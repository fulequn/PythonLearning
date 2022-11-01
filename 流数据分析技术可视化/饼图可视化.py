# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 23:12:22 2020

@author: 23820
"""

from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

keys=['优秀', '差', '良好']
values=[362, 130, 2803]
# with open("3Discretization.txt", 'r', encoding='utf-8') as f:
#     for i in f:
#         left = i.find(',')
#         right = i.rfind(',')
#         keys.append(i[left+1:right])
#         values.append(i[right+1:-2])

#数据统计
# d = {}
# for i in values:
#     if i == '优秀':
#         d['优秀'] = d.get('优秀', 0)+1
#     elif i == '良好':
#         d['良好'] = d.get('良好', 0)+1
#     elif i == '差':
#         d['差'] = d.get('差', 0)+1

c = (
    Pie()
    .add("", [list(z) for z in zip(keys, values)])
    # .add("", [list(z) for z in d])
    .set_colors(["red", "#9400D3", "orange"])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="电影评分总体展示",
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
    .render("电影评分总体展示.html")
)

movie_type=[]
movie_num=[]
with open("4CountOfMoivesByType.txt", 'r', encoding='utf-8') as f:
    for i in f:
        comma = i.find(',')
        movie_type.append(i[1:comma])
        movie_num.append(i[comma+1:-2])
        
c = (
    Pie(init_opts=opts.InitOpts(width="1500px", height="800px"))
    .add("", [list(z) for z in zip(movie_type, movie_num)])
    # .add("", [list(z) for z in d])
    # .set_colors(["red", "#9400D3", "orange","blue", "green", "yellow", "red", "pink", "orange", "purple"])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="各类型电影的数量",
            pos_left="center",
            pos_top='top',
            title_textstyle_opts=opts.TextStyleOpts(font_size=25)         
            ),
        legend_opts=opts.LegendOpts(
            type_="scroll", 
            pos_left="85%", 
            pos_top="20%",
            orient="vertical",
            textstyle_opts=opts.TextStyleOpts(font_size=16) 
            ),
        )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("各类型电影的数量.html")
)
