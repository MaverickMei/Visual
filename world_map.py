#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# -------------------------------
# Time   ：2020/2/21  15:21
# Author ：Jerry Mei, ECNU
# Email  ：meicczj@163.com
# IDE    ：PyCharm
# -------------------------------
from pyecharts.charts import Map
from pyecharts import options as opts
from pyecharts.faker import Faker

c = (Map()
    .add("商家A", [list(z) for z in zip(Faker.country, Faker.values())], "world")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
    title_opts=opts.TitleOpts(title="Map-世界地图"),
    visualmap_opts=opts.VisualMapOpts(max_=200),)
    )
c.render('map2.html')