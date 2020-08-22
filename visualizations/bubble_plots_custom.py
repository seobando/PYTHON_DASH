import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd

df = pd.read_csv('Data/mpg.csv')

data = [go.Scatter(         
    x=df['horsepower'],
    y=df['mpg'],
    text=df['name'],
    mode='markers',
    marker=dict(size=df['weight']/100,
    color=df['cylinders'],
    showscale = True
    ) 
)]

layout = go.Layout(title='Bubble Chart',hovermade='closest')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubble2.html')


