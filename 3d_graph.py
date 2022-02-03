# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 20:40:11 2021

@author: Dmytro
"""

import pandas as pd
import plotly.express as px
import math
from numba import jit, cuda

# ax = plt.axes(projection='3d')


zdata = []
xdata = []
ydata =[]
color = []

for z in range (1,11):
    for x in range (1,11):
        for y in range (1,11):
            zdata.append(z)
            xdata.append(x)
            ydata.append(y)
            

points_df = pd.DataFrame(xdata, columns=['x'])
points_df['y'] = ydata
points_df['z'] = zdata


def distance (x1,x2,y1,y2,z1,z2):
    distance = math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
    print(distance)
    
    
for index, row in points_df.iterrows():
    # print(row['x'], row['y'], row['z'])
    x1 = row['x']
    y1 = row['y']
    z1 = row['z']
    
    for index, row in points_df.iterrows():
        x2 = row['x']
        y2 = row['y']
        z2 = row['z']
        if 0<(x1-x2)<1:
            color.append(distance(x1, x2, y1, y2, z1, z2))
            empty = 1
            break
        else:
            empty = 0
    if empty == 0:
        color.append(0)
    else:
        empty = 0

points_df['color'] = color


fig = px.scatter_3d(points_df, x='x', y='y', z='z',
              color='color')
with open('p_graph.html', 'a') as f:
    f.write(fig.to_html(full_html=False, include_plotlyjs='cdn'))



