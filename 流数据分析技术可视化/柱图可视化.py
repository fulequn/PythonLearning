# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 22:28:29 2020

@author: 23820
"""

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot

rawyears=[]
data=[]
with open("1CountOfMoivesByYear.txt", 'r', encoding='utf-8') as f:
    for i in f:
        comma = i.find(',')
        rawyears.append(i[1:comma])
        data.append(i[comma+1:-2])
    
years = ["{}年".format(i) for i in rawyears]

c = (
    Bar()
    .add_xaxis(years)
    .add_yaxis("电影发布数量", data)
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="每年发行电影的数量"
            ),
        datazoom_opts=opts.DataZoomOpts(),
    )
    .render("每年发行电影的数量.html")
)

movieName=['Toy Story', 'Jumanji', 'Grumpier Old Men',
           'Waiting to Exhale', 'Father of the Bride Part II', 'Heat', 'Sabrina']
data=[4.1468463, 3.201141, 3.0167365, 2.7294118, 3.0067568
      ,3.8787234, 3.4104803]

c = (
    Bar()
    .add_xaxis(movieName)
    .add_yaxis("电影平均分", data)
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="每部电影的平均分"
            ),
        xaxis_opts=opts.AxisOpts(
            type_='category',
            axislabel_opts={"interval":"0","rotate":20},
            name='电影名称',
        ),
        # datazoom_opts=opts.DataZoomOpts(),
    )
    .render("每部电影的平均分.html")
)
# make_snapshot(snapshot, c.render(), "每部电影的平均分.png")