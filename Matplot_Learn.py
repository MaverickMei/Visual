#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time   :  14:57
# Author : Jerry Mei

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np


def f(x, y):
     return np.sin(np.sqrt(x ** 2 + y ** 2))


x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
# 调整观察角度和方位角。这里将俯仰角设为60度，把方位角调整为35度
ax.view_init(60, 35)

plt.show()