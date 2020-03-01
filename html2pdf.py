#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# -------------------------------
# Time   ：2020/2/23  11:37
# Author ：Jerry Mei, ECNU
# Email  ：meicczj@163.com
# IDE    ：PyCharm
# -------------------------------
import pdfkit
path_wk = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf = path_wk)
pdfkit.from_file(r'E:\Desktop\charts.html', r'E:\Desktop\out.pdf',configuration=config)
