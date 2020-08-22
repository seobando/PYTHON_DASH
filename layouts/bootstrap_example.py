import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np


#---------------------------------- LAYER 1 - DATA ----------------------------------#
np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

plot_1 = dcc.Graph(id='scatterplot',
                    figure = {'data':[
                            go.Scatter(
                            x=random_x,
                            y=random_y,
                            mode='markers',
                            marker = {
                                'size':12,
                                'color': 'rgb(51,204,153)',
                                'symbol':'pentagon',
                                'line':{'width':2}
                            }
                            )],
                    'layout':go.Layout(title='My Scatterplot',
                                        xaxis = {'title':'Some X title'},
                                        height =  600)}
                    )

plot_2 = dcc.Graph(id='scatterplot_2',
                    figure = {'data':[
                            go.Scatter(
                            x=random_x,
                            y=random_y,
                            mode='markers',
                            marker = {
                                'size':12,
                                'color': 'rgb(51,204,153)',
                                'symbol':'pentagon',
                                'line':{'width':2}
                            }
                            )],
                    'layout':go.Layout(title='My Scatterplot',
                                        xaxis = {'title':'Some X title'})}
                    )

plot_3 = dcc.Graph(id='scatterplot_3',
                    figure = {'data':[
                            go.Scatter(
                            x=random_x,
                            y=random_y,
                            mode='markers',
                            marker = {
                                'size':12,
                                'color': 'rgb(51,204,153)',
                                'symbol':'pentagon',
                                'line':{'width':2}
                            }
                            )],
                    'layout':go.Layout(title='My Scatterplot',
                                        xaxis = {'title':'Some X title'})}
                    )

plot_4 = dcc.Graph(id='scatterplot_4',
                    figure = {'data':[
                            go.Scatter(
                            x=random_x,
                            y=random_y,
                            mode='markers',
                            marker = {
                                'size':12,
                                'color': 'rgb(51,204,153)',
                                'symbol':'pentagon',
                                'line':{'width':2}
                            }
                            )],
                    'layout':go.Layout(title='My Scatterplot',
                                        xaxis = {'title':'Some X title'})}
                    )                                                              

#---------------------------------- LAYER 2 - LAYOUT ----------------------------------#

# Based in https://dash-gallery.plotly.host/dash-oil-and-gas/

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

card_content = [
    dbc.CardBody(
        [
            html.H5("Card title", className="card-title"),
        ]
    ),
    dbc.CardFooter("This is the footer")
]

body = html.Div([

    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'paddingBottom': 25, 
            'paddingTop': 25
        }
    ),

    dbc.Row([

            dbc.Col(html.Div(plot_1),width=4), 

            dbc.Col(
                [
                    dbc.Row([
                        
                        dbc.Col(dbc.Card(card_content, color="secondary", inverse=True)),
                        dbc.Col(dbc.Card(card_content, color="secondary", inverse=True)),
                        dbc.Col(dbc.Card(card_content, color="secondary", inverse=True)),
                        dbc.Col(dbc.Card(card_content, color="secondary", inverse=True))

                    ],className="mb-4"), 
                    dbc.Row([
 
                        dbc.Col(html.Div(plot_2))
                        
                        ])
                
                ],width=8)
            ]), 
        
        dbc.Row([
            dbc.Col(html.Div(plot_3,style={'marginBottom': 25, 'marginTop': 25}),width=8), 
            dbc.Col(html.Div(plot_4,style={'marginBottom': 25, 'marginTop': 25}),width=4)
            ])     

    ], 
    style={
        'backgroundColor':'#f2f2f2',
        'paddingLeft':50,
        'paddingRight':50,
        'paddingBottom':50,
        'height':'100%'
        }) 

app.layout = html.Div([body])

#---------------------------------- LAYER 3 - CALLBACKS ----------------------------------#


if __name__ == "__main__":
    app.run_server(debug = True)
