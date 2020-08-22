# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Create a pandas DataFrame from 2010YumaAZ.csv
df = pd.read_csv('../data/2010YumaAZ.csv')
days = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']

# Use a for loop to create the traces for the seven days
# There are many ways to do this! Could also do this with a
# list comprehension.

data = []

for day in days:
    trace = go.Scatter(x=df['LST_TIME'],
                       y=df[df['DAY']==day]['T_HR_AVG'],
                       mode='lines',
                       name=day)
    data.append(trace)

# Define the layout
layout = go.Layout(
    title='Daily temperatures from June 1-7, 2010 in Yuma, Arizona',
    hovermode='closest'
)

# Create a fig from data and layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='solution2a.html')