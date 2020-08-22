
# 1. What's Dash?

"Dash is the most downloaded, trusted framework for building ML & data science web apps".

from: https://plotly.com/dash/

# 2. Set up

1. Install Anaconda:

https://www.anaconda.com/products/individual#macos

2. Create project directory


3. Create conda environment:

```
conda create --name mydashenv python=3.7.6
```

4. Activate virtual environment:

```
conda activate mydashenv
```

5. Install requirements:

```
pip install -r requirements.txt
```

6. Test dash installation:

```
python
import dash
```

7. Hello world!

```python
import dash
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    dbc.Alert("Hello Bootstrap!", color="success"),
    className="p-5",
)

if __name__ == "__main__":
    app.run_server()
```

8. Start Server

```
python3 app.py
```

## 3. Project structure

1. Import libraries
2. Get Data
3. Set Graphs, Charts and Tables
4. Set Filters
5. Set layout
6. Set callbacks
7. Run app

# 3. Layout

## Bootstrap Example:

```python
body = html.Div([

    html.H1("Bootstrap Grid System Example"),

    dbc.Row(dbc.Col(html.Div(dbc.Alert("This is one column", color="primary")))),
         
    dbc.Row([

            dbc.Col(html.Div(dbc.Alert("One of three columns", color="primary")),width=4),
            dbc.Col(
                [
                    dbc.Row([
                        
                        dbc.Col(html.Div(dbc.Alert("One of three columns", color="primary"))),
                        dbc.Col(html.Div(dbc.Alert("One of three columns", color="primary"))),
                        dbc.Col(html.Div(dbc.Alert("One of three columns", color="primary"))),
                        dbc.Col(html.Div(dbc.Alert("One of three columns", color="primary"))),
                        dbc.Col(html.Div(dbc.Alert("One of three columns", color="primary"))),    
                        dbc.Col(html.Div(dbc.Alert("One of three columns", color="primary"))) 

                    ]),
                    
                    dbc.Row([
 
                        dbc.Col(html.Div(dbc.Alert("One of three columns", color="primary")))
                        
                        ])
                
                ],width=8)
            ]),

    dbc.Row([
            dbc.Col(html.Div(dbc.Alert("One of three columns", color="primary")),width=8),
            dbc.Col(html.Div(dbc.Alert("One of three columns", color="primary")),width=4)
            ]),

    dbc.Row([
            dbc.Col(html.Div(dbc.Alert("One of three columns", color="primary")),width=8),
            dbc.Col(html.Div(dbc.Alert("One of three columns", color="primary")),width=4)
            ])      
    ]) 
     

app.layout = html.Div([body])
```

## Fit sizes with cards:

### Play with height:

```python
app.layout = html.Div([
    dbc.Container([
            dbc.Row([html.H1('title')]),
            dbc.Row([
                dbc.Col([dbc.Card(LEFT_MENU, style={'height':'100vh'})]),
                dbc.Col([dbc.Card(GRAPHS, style={'height':'100vh'})])  
])])])
```

### Card Grouping

```python
app.layout = html.Div([
    dbc.Container([
            dbc.Row([html.H1('title')]),
            dbc.Row([
                dbc.CardGroup([
                    dbc.Card(LEFT_MENU),
                    dbc.Card(GRAPHS)
                ]) 
            ])
    ])
```

Resources: https://stackoverflow.com/questions/60673007/how-to-make-a-card-fill-screen-height

# 4. Graphs, Charts, Tables and Widgets

## 4.1 Scatter Plots:

```python
import numpy as np
import plotly.offline as pyo 
import plotly.graph_objs as go 

np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data = [go.Scatter(
    x=random_x,
    y=random_y,
    mode='markers',
    marker=dict(
        size=12,
        color='rgb(51,204,153)',
        symbol='pentagon',
        line={'width':2}
    ))]

layout = go.Layout(
    title='Hello First Plot',
    xaxis={'title':'MY X AXIS'},
    yaxis=dict(title='MY Y AXIS'),
    hovermode='closest')

fig = go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='scatter.html')
```

## 4.2. Line Charts:

```python
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

np.random.seed(56)
x_values = np.linspace(0, 1, 100) # 100 evenly spaced values
y_values = np.random.randn(100)   # 100 random values

# create traces
trace0 = go.Scatter(
    x = x_values,
    y = y_values+5,
    mode = 'markers',
    name = 'markers'
)
trace1 = go.Scatter(
    x = x_values,
    y = y_values,
    mode = 'lines+markers',
    name = 'lines+markers'
)
trace2 = go.Scatter(
    x = x_values,
    y = y_values-5,
    mode = 'lines',
    name = 'lines'
)
data = [trace0, trace1, trace2]  # assign traces to data
layout = go.Layout(
    title = 'Line chart showing three different modes'
)
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig, filename='line1.html')

```

## 4.3. Bar Charts:

```python
import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd

df = pd.read_csv('Data/2018WinterOlympics.csv')
print(df)

data = [go.Bar(x=df['NOC'],y=df['Total'])]
layout = go.Layout(title='Medals')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)
```

## 4.4. Bublet Plots:

```python
import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd

df = pd.read_csv('Data/mpg.csv')

data = [go.Scatter(          # start with a normal scatter plot
    x=df['horsepower'],
    y=df['mpg'],
    text=df['name'],
    mode='markers',
    marker=dict(size=1.5*df['cylinders']) # set the marker size
)]

layout = go.Layout(
    title='Vehicle mpg vs. horsepower',
    xaxis = dict(title = 'horsepower'), # x-axis label
    yaxis = dict(title = 'mpg'),        # y-axis label
    hovermode='closest'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubble1.html')
```

## 4.5. Box plots:

```python
import plotly.offline as pyo
import plotly.graph_objs as go

snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]

data = [
    go.Box(
        y=snodgrass,
        name='QCS'
    ),
    go.Box(
        y=twain,
        name='MT'
    )
]
layout = go.Layout(
    title = 'Comparison of three-letter-word frequencies<br>\
    between Quintus Curtius Snodgrass and Mark Twain'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='box3.html')
```

## 4.6. Histograms:

```python
import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd 

df = pd.read_csv('Data/mpg.csv')

data = [go.Histogram(x=df['mpg'],xbins=dict(start=0,end=50,size=2))]

layout = go.Layout(title='Histogram')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)
```

## 4.7. Displots:

```python
import plotly.offline as pyo 
import plotly.figure_factory as ff
import numpy as np

x = np.random.randn(1000)

hist_data = [x]
group_labels = ['distplot']

fig = ff.create_distplot(hist_data, group_labels)
pyo.plot(fig)
```

## 4.8. Heatmaps:

```python
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
```

## 4.9. PieChart:

```python
import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd

labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
values = [4500, 2500, 1053, 500]

data = [
        go.Pie(
            labels=labels, 
            values=values
            )
        ]

layout = go.Layout(
    title = 'Gas participations'
)

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='pie.html')
```

## 4.10 Donut chart:

```python
import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd

labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
values = [4500, 2500, 1053, 500]

data = [
        go.Pie(
            labels=labels, 
            values=values,
            hole=.7
            )
        ]

layout = go.Layout(
    title = 'Gas participations'
)

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='donut.html')
```

## 4.10. Tables:

```python
import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv')

fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns)),
    cells=dict(values=[df.Rank, df.State, df.Postal, df.Population]))
])
pyo.plot(fig, filename='table.html')
```

Resources: https://plotly.com/python/

# 5. Filters

## Basic filters:

```python

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([

    # DROPDOWN https://dash.plot.ly/dash-core-components/dropdown
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),

    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF'],
        multi=True
    ),

    # SLIDER https://dash.plot.ly/dash-core-components/slider
    html.Label('Slider'),
    html.P(
    dcc.Slider(
        min=-5,
        max=10,
        step=0.5,
        marks={i: i for i in range(-5,11)},
        value=-3
    )),

    # RADIO ITEMS https://dash.plot.ly/dash-core-components/radioitems
    html.Label('Radio Items'),
    dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    )
], style={'width': '50%'})

if __name__ == '__main__':
    app.run_server()
    
```    

# 6. Callbacks

## Single filters:

```python
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('gapminderDataFiveYear.csv')

app = dash.Dash()

# https://dash.plot.ly/dash-core-components/dropdown
# We need to construct a dictionary of dropdown values for the years
year_options = []
for year in df['year'].unique():
    year_options.append({'label':str(year),'value':year})

app.layout = html.Div([
    dcc.Graph(id='graph'),
    dcc.Dropdown(id='year-picker',options=year_options,value=df['year'].min())
])

@app.callback(Output('graph', 'figure'),
              [Input('year-picker', 'value')])
def update_figure(selected_year):
    filtered_df = df[df['year'] == selected_year]
    traces = []
    for continent_name in filtered_df['continent'].unique():
        df_by_continent = filtered_df[filtered_df['continent'] == continent_name]
        traces.append(go.Scatter(
            x=df_by_continent['gdpPercap'],
            y=df_by_continent['lifeExp'],
            text=df_by_continent['country'],
            mode='markers',
            opacity=0.7,
            marker={'size': 15},
            name=continent_name
        ))

    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'type': 'log', 'title': 'GDP Per Capita'},
            yaxis={'title': 'Life Expectancy'},
            hovermode='closest'
        )
    }

if __name__ == '__main__':
    app.run_server()
```

## Multiple filters:

```python
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('Data/mpg.csv')

app = dash.Dash()

features = df.columns

app.layout = html.Div([

                html.Div([
                    dcc.Dropdown(
                        id = 'xaxis',
                        options= [{'label':i,'value':i} for i in features],
                        value='displacement')
                ],style={'width':'48%','display':'inline-block'}),

                html.Div([
                    dcc.Dropdown(
                        id = 'yaxis',
                        options= [{'label':i,'value':i} for i in features],
                        value='mpg')
                ],style={'width':'48%','display':'inline-block'}),

                dcc.Graph(id='feature-graphic')

],style={'padding':10})

@app.callback(Output('feature-graphic','figure'),
               [Input('xaxis','value'),
               Input('yaxis','value')])
def update_graph(xaxis_name,yaxis_name):

    data = [
        go.Scatter(
            x=df[xaxis_name],
            y=df[yaxis_name],
            text=df['name'],
            mode = 'markers',
            marker = {'size':15,
                      'opacity':0.5,
                      'line':{'width':0.5,'color':'white'}  },
        )
    ]

    layout = go.Layout(
                        title='My Dashboard for MPG',
                        xaxis={'title':xaxis_name},
                        yaxis={'title':yaxis_name},
                        hovermode='closest'
                    )

    return {'data': data,'layout':layout}


if __name__ == '__main__':
    app.run_server()
```    

## Datepickers and multiple selection filter

```python
import dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input,Output,State
import pandas_datareader.data as web
from datetime import datetime
import pandas as pd
import os

os.environ['ALPHAVANTAGE_API_KEY'] = 'YOUR_API_KEY'

app = dash.Dash()

nsdq = pd.read_csv('Data/NASDAQcompanylist.csv')
nsdq.set_index('Symbol',inplace=True)
options = []

for tic in nsdq.index:
    mydict = {}
    mydict['label'] = str(nsdq.loc[tic]['Name']) + ' ' + tic
    mydict['value'] = tic
    options.append(mydict)

app.layout = html.Div([
    html.H1('Stock Ticker Dashboard'),
    html.Div([
        html.H3('Select stock symbols:', style={'paddingRight':'30px'}),
        dcc.Dropdown(
            id='my_ticker_symbol',
            options=options,
            value=['TSLA'],
            multi=True
        )
    ], style={'display':'inline-block', 'verticalAlign':'top', 'width':'30%'}),
    html.Div([
        html.H3('Select start and end dates:'),
        dcc.DatePickerRange(
            id='my_date_picker',
            min_date_allowed=datetime(2015, 1, 1),
            max_date_allowed=datetime.today(),
            start_date=datetime(2018, 1, 1),
            end_date=datetime.today()
        )
    ], style={'display':'inline-block'}),
    html.Div([
        html.Button(
            id='submit-button',
            n_clicks=0,
            children='Submit',
            style={'fontSize':24, 'marginLeft':'30px'}
        ),
    ], style={'display':'inline-block'}),
    dcc.Graph(
        id='my_graph',
        figure={
            'data': [
                {'x': [1,2], 'y': [3,1]}
            ]
        }
    )
])
@app.callback(
    Output('my_graph', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [State('my_ticker_symbol', 'value'),
    State('my_date_picker', 'start_date'),
    State('my_date_picker', 'end_date')])
def update_graph(n_clicks, stock_ticker, start_date, end_date):
    start = datetime.strptime(start_date[:10], '%Y-%m-%d')
    end = datetime.strptime(end_date[:10], '%Y-%m-%d')
    traces = []
    for tic in stock_ticker:
        df = web.DataReader(tic,'av-daily',start,end)
        traces.append({'x':df.index, 'y': df.close, 'name':tic})
    fig = {
        'data': traces,
        'layout': {'title':', '.join(stock_ticker)+' Closing Prices'}
    }
    return fig

if __name__ == '__main__':
    app.run_server()
```

# 7. Live updating

```python
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    html.H1(id='live-update-text'),
    dcc.Interval(
        id='interval-component',
        interval=2000, # 2000 milliseconds = 2 seconds
        n_intervals=0
    )
])

@app.callback(Output('live-update-text', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_layout(n):
    return 'Crash free for {} refreshes'.format(n)

if __name__ == '__main__':
    app.run_server()
```

# 8. Resources

- Setup: 
    - https://www.udemy.com/course/interactive-python-dashboards-with-plotly-and-dash/learn/lecture/9569964#overview
- Indicators:
    - https://plotly.com/python/indicator/
- Layout: 
  - https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/
  -  https://medium.com/swlh/dashboards-in-python-for-beginners-using-dash-responsive-mobile-dashboards-with-bootstrap-css-2a0d05a53cf6
- Examples:
    - https://github.com/Pierian-Data/Plotly-Dashboards-with-Dash
    - https://dash-gallery.plotly.host/Portal/
    - https://github.com/plotly/dash-sample-apps
- Visualization library:
   -  https://plotly.com/python/basic-charts/
