
import dash
import dash_daq as daq
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('SimpleExample', external_stylesheets=external_stylesheets)


app.layout = html.Div(children=[
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5],
                    'type': 'bar', 'name': u'Montréal'},
            ],
        }
    )
])


app = DjangoDash('Pizza', external_stylesheets=external_stylesheets)

app.layout = html.Div([
    daq.Thermometer(
        value=5,
        scale={'start': 2, 'interval': 3,
               'labelInterval': 2, 'custom': {
                   '2': 'ideal temperature',
                   '5': 'projected temperature'
               }}
    )
])
