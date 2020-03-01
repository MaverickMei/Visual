#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# -------------------------------
# Time   ：2020/2/21  15:02
# Author ：Jerry Mei, ECNU
# Email  ：meicczj@163.com
# IDE    ：PyCharm
# -------------------------------
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import EffectScatter
from pyecharts.globals import SymbolType
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
import matplotlib.pyplot as plt
import matplotlib.image as image
import os


def effectscatter_base() -> EffectScatter:
    c = (
        EffectScatter()
        .add_xaxis(Faker.choose())
        .add_yaxis("", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts(title="EffectScatter-基本示例"))
    )
    return c

Infile=effectscatter_base().render()
Outfile_temp='p123.png'

make_snapshot(snapshot,Infile,Outfile_temp,delay=2,pixel_ratio=1,is_remove_html=False,browser= "Chrome")
img = image.imread('p123.png', 'png')
imgplot = plt.imshow(img)
# os.remove(Outfile_temp)

