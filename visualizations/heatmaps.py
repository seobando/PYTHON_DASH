import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('Data/2010SantaBarbaraCA.csv')

data = [go.Heatmap(
    x=df['DAY'],
    y=df['LST_TIME'],
    z=df['T_HR_AVG'],
    colorscale='Jet'
)]

layout = go.Layout(
    title='Santa Barbara, CA USA'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='Santa_Barbara.html')

