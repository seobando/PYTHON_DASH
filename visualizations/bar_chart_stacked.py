import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd

df = pd.read_csv('Data/2018WinterOlympics.csv')

trace_1 = go.Bar(x=df['NOC'],y=df['Gold'], name='Gold', marker={'color':'#FFD700'})
trace_2 = go.Bar(x=df['NOC'],y=df['Silver'], name='Silver', marker={'color':'#9EA0A1'})
trace_3 = go.Bar(x=df['NOC'],y=df['Bronze'], name='Bronze', marker={'color':'#CD7F32'})

data = [trace_1,trace_2,trace_3]
layout = go.Layout(title='Medals',barmode='stack')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)