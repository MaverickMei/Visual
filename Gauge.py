#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#-------------------------------
# Time   ：2020/1/2  21:05
# Author ：Jerry Mei, ECNU
# Email  ：meicczj@163.com
# IDE    ：PyCharm
#-------------------------------
from pyecharts import options as opts
from pyecharts.charts import Gauge, Page


def gauge_base() -> Gauge:
    c = (
        Gauge()
        .add("", [("完成率", 66.6)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Gauge-基本示例"))
    )
    return c

gauge_base().render(r"E:\Desktop\Gauge.html")