#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time   :  15:34
# Author : Jerry Mei

from pyecharts.charts import Map
from pyecharts import options as opts

#  将数据处理成列表
locate = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '陕西', '甘肃', '青海', '宁夏', '新疆']
GDP_1978 = [108.84,82.65,183.06,87.99,58.04,229.20,81.98,174.80,272.81,249.24,123.72,114.10,66.37,87.00,225.45,162.92,151.00,146.99,185.85,75.85,16.40,67.32,184.61,46.62,69.05,81.07,64.73,15.54,13.00,39.07]
GDP_2017 = [28014.94,18549.19,34016.32,15528.42,16096.21,23409.24,14944.53,15902.68,30632.99,85869.76,51768.26,27018,32182.09,20006.31,72634.15,44552.83,35478.09,33902.96,89705.23,18523.26,4462.54,19424.73,36980.22,13540.83,16376.34,21898.81,7459.9,2624.83,3443.56,10881.96]
list1 = [[locate[i],GDP_1978[i]] for i in range(len(locate))]
list2 = [[locate[i],GDP_2017[i]] for i in range(len(locate))]
#  最终生成[['北京',108.84],[],[].....]的list

map_1 = Map()

title_opts = opts.TitleOpts(title='1978年和2017年全国各省GDP',
                            # subtitle='副标题：\n    --和上一年对比',
                            # title_link='https://pyecharts.org',
                            subtitle_link=None,
                            pos_left='35%',
                            pos_right='35%',
                            pos_top='95%',
                            pos_bottom='0',
                            # title_textstyle_opts=opts.TextStyleOpts(color='red',
                            #                                         font_style='normal',  # 风格：'normal'，'italic'，'oblique'
                            #                                         font_weight='bolder', # 粗细：'normal'，'bold'，'bolder'，'lighter'
                            #                                         font_family='黑体',  # 字体还可以是 'serif' , 'monospace', 'Arial', 'Courier New', 'Microsoft YaHei', ...
                            #                                         font_size=18, # 字号：num类型
                            #                                         )
                            )
map_1.set_global_opts(
    title_opts=title_opts,
    visualmap_opts=opts.VisualMapOpts(max_=100000)  # 最大数据范围
    )
map_1.add("2017年各省GDP", list2, maptype="china")
map_1.add("1978年各省GDP", list1, maptype="china")
map_1.render('map1.html')
