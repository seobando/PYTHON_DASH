import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd

df = pd.read_csv('Data/2018WinterOlympics.csv')
print(df)

data = [go.Bar(x=df['NOC'],y=df['Total'])]
layout = go.Layout(title='Medals')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)

