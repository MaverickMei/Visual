#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# -------------------------------
# Time   ：2020/1/1  21:51
# Author ：Jerry Mei, ECNU
# Email  ：meicczj@163.com
# IDE    ：PyCharm
# -------------------------------

from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType, RenderType

init_opts = opts.InitOpts(width='1000px', height='600px', chart_id=None, renderer=RenderType.CANVAS,
                          page_title='网页标题：班级成绩柱状图', theme=ThemeType.DARK, bg_color=None)
bar = Bar(init_opts)

bar.add_xaxis(["小明", "小红", "丁丁", "小白", "小黑", "小小"])
bar.add_yaxis("期中成绩", [75, 90, 90, 70, 70, 90])
bar.add_yaxis("期末成绩", [85, 100, 96, 80, 75, 90])

title_opts = opts.TitleOpts(title='主标题：班级成绩',
                            subtitle='副标题：\n    --期中期末',
                            title_link='https://pyecharts.org',
                            subtitle_link=None, pos_left='45%',
                            pos_right='45%', pos_top='95%',
                            pos_bottom='0',
                            title_textstyle_opts=opts.TextStyleOpts(color='red',
                                                                    font_style='normal',# 风格：'normal'，'italic'，'oblique'
                                                                    font_weight='bolder', # 粗细：'normal'，'bold'，'bolder'，'lighter'
                                                                    font_family='黑体',  # 字体还可以是 'serif' , 'monospace', 'Arial', 'Courier New', 'Microsoft YaHei', ...
                                                                    font_size=18, # 字号：num类型
                                                                    )
                            )
bar.set_global_opts(title_opts)

bar.render(r"E:\Desktop\bar.html")
