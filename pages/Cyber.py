import dash_html_components as html
from utils import Header
import pandas as pd
import pathlib
import app as app
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_renderer
import dash_table
import datetime
import pandas as pd
import plotly.graph_objs as go
import flask
import networkx as nx
import numpy as np
import plotly.express as px
import os
import mysql.connector
import plotly
import random
import plotly.graph_objs as go
from collections import deque

from utils import Header
import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()
cyber_datatable = pd.read_csv(DATA_PATH.joinpath("cyber-data.csv"))
alert_table = pd.read_csv(DATA_PATH.joinpath("table-alert.csv"))
df_map = pd.read_csv(DATA_PATH.joinpath("cp-sam-map.csv"))
lat_site = df_map.Latitude
lon_site = df_map.Longitude
nodes_df = df_map.Nodes
fig = go.Figure(go.Scattermapbox(
    mode="markers+lines",
    lat=lat_site,
    lon=lon_site,
    marker={'size': 12},
    text=nodes_df,
    hoverinfo='text'))
fig.add_trace(go.Scattermapbox(
    lat=[46.730651],
    lon=[-117.169465],
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=28,
        color='rgb(105,105,105)',
        opacity=0.3
    ),
))
fig.update_layout(
    showlegend=False,
    height=550,
    margin={'l': 0, 't': 0, 'b': 0, 'r': 0},
    mapbox={
        'style': "carto-positron",
        'center': {'lon': -117.1694051, 'lat': 46.730651},
        'zoom': 13})

np.random.seed(1)

N = 100
N1 = 50
random_x = np.linspace(10, 100)
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N) + 5
random_y3 = np.random.randn(N1)

# Create traces
fig_2 = go.Figure()
fig_2.add_trace(go.Scatter(x=random_x, y=random_y1,
                           mode='lines+markers',
                           name='lines+markers'))


def create_layout(app):
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 2
            html.Div([
                html.Div([
                    html.Div([
                        html.Div([
                            html.Div([
                                html.H6(["Cyber Resiliency Score"]),
                                html.P(["96.03 (-1.05)"])
                            ], className="pr-score"),

                            html.Div([
                                html.Div([
                                    html.H5(["Cyber Resiliency Score"]),
                                    html.P(["(Live graph)"]),
                                ], className="pr-score"),
                                html.Div([
                                    dcc.Graph(id="pr-graph", figure=fig_2),
                                ], className="Graph-cr")
                            ], className="cr-graph"),

                            html.Div([
                                html.Table(
                                    dash_table.DataTable(id="pr-alert",
                                                         columns=[{"name": i, "id": i, "selectable": True} for i in
                                                                  alert_table.columns],
                                                         selected_rows=[],
                                                         style_cell={'padding': '5px'},
                                                         style_data_conditional=[
                                                             {'if': {'row_index': 'even'},
                                                              'backgroundColor': 'rgb(94, 128, 63)'},
                                                             {'if': {'row_index': 'odd'},
                                                              'backgroundColor': 'rgb(176, 35, 24)'}],
                                                         style_header={
                                                             'backgroundColor': 'rgb(246, 193, 67)',
                                                             'fontWeight': 'bold',
                                                             'text-align': 'center'
                                                         }, page_size=6, page_action="native",
                                                         data=alert_table.to_dict('records'),
                                                         selected_columns=["1", "2"]),
                                ),
                            ], className="pr-table"),
                        ], className="container"),
                    ], className="one-third column"),

                    html.Div([
                        html.Div([
                            dash_table.DataTable(id="pr-table",
                                                 columns=[{"name": i, "id": i, "selectable": True} for i in
                                                          cyber_datatable.columns],
                                                 selected_rows=[],
                                                 style_cell={'padding-top': '30px', 'padding-bottom': '30px'},
                                                 style_data_conditional=[
                                                     {'if': {'row_index': 'odd'},
                                                      'backgroundColor': 'rgb(248, 248, 248)'}],
                                                 style_header={
                                                     'backgroundColor': 'rgb(152, 21, 27)',
                                                     'fontWeight': 'bold',
                                                     'text-align': 'center'
                                                 }, page_size=6, page_action="native",
                                                 data=cyber_datatable.to_dict('records'),
                                                 selected_columns=["1", "2"]),
                        ], className="container")
                    ], className="one-third column"),

                    html.Div([
                        html.Div([
                            html.Div([
                                dcc.Graph(id="graph-phy", figure=fig)
                            ], className="maps-physical"),
                        ], className="container")
                    ], className="one-third column maps-con"),

                ], className='row')
            ], className="page")
        ]
    )
