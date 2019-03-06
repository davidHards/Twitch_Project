import plotly.plotly as py
import plotly.figure_factory as ff
import pandas as pd

import os

path = os.path.abspath(r'D:/UG_Project_Data/streamViewCount0.csv')

df = pd.read_csv(path)

table = ff.create_table(df)
py.iplot(table, filename='streams')
# cdf ccdf

# latex

#overleaf
