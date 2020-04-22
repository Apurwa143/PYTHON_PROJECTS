import pandas as pd
from scipy.interpolate import interp1d
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('time_covid.csv')
list1 = df.cases.values.tolist()
m = interp1d([1, max(list1)], [5, 18])
circle_radius = m(list1)
typelist = ['open-street-map', 'white-bg', 'carto-positron', 'carto-darkmatter', 'stamen-terrain', 'stamen-toner', 'stamen-watercolor']
fig = px.density_mapbox(df, lat='Lat', lon='Long', radius=circle_radius, zoom=0, mapbox_style='stamen-toner')
fig.show()

