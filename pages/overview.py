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

## Connecting to database In local host##
# SyncAED_db = mysql.connector.connect(host="localhost", user="root", passwd="Classmate123@#", database="Sync_AED")
# mycursor = SyncAED_db.cursor()

### Acquistion of the Anomaly Data Table from database ##
# anomaly_QUERY = 'SELECT * FROM Sync_AED.`anomaly_dect_data`'
# df_anomaly = pd.read_sql_query(anomaly_QUERY, SyncAED_db)

## Connection from database for Displaying Bus Map ##
# bus_data_14 = 'SELECT * FROM Sync_AED.`bus-data`'
# bus_data_14_map = pd.read_sql_query(bus_data_14, SyncAED_db)

# us_cities = pd.read_csv(DATA_PATH.joinpath("us-cities-top-1k.csv"))
# us_cities = us_cities.query("State in ['New York', 'Ohio']")

cp_sam_graph = pd.read_csv(DATA_PATH.joinpath("Book2.csv"))

df_map = pd.read_csv(DATA_PATH.joinpath("cp-sam-map.csv"))
lat_site = df_map.Latitude
lon_site = df_map.Longitude
nodes_df = df_map.Nodes
# fig = px.scatter_mapbox(df_map, lat="Latitude", lon="Longitude",
# color_discrete_sequence=["#98151B"], zoom=6, height=550)

# fig = px.line_mapbox(df_map, lat="Latitude", lon="Longitude", zoom=3, height=500)

# fig.update_layout(mapbox_style="carto-positron", mapbox_zoom=13, mapbox_center_lat = 46.73613, mapbox_center_lon = -117.1556,
# margin={"r":0,"t":0,"l":0,"b":0})


import plotly.graph_objects as go

fig = go.Figure(go.Scattermapbox(
    mode="markers+lines",
    lat=lat_site,
    lon=lon_site,
    marker={'size': 12},
    text=nodes_df,
    hoverinfo='text'))

fig.update_layout(
    height=550,
    margin={'l': 0, 't': 0, 'b': 0, 'r': 0},
    mapbox={
        'style': "carto-positron",
        'center': {'lon': -117.155, 'lat': 46.736},
        'zoom': 12})

# df_map = df_map.query("Longitude in ['-117.225414', '-118.436876']" )
# fig = px.scatter_mapbox(df_map, lat="Latitude", lon="Longitude",hover_name='Nodes',
# color_discrete_sequence=["#98151b"], zoom=6, height=550, size_max=40)
# fig.update_layout(mapbox_style="carto-positron")
# fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})


fig_cp_sam = px.line(cp_sam_graph, x='Time', y='CP-SAM')

df_data = pd.read_csv(DATA_PATH.joinpath("Data-1-anomaly.csv"))


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    html.Div([
                        html.Div([
                            html.Div([
                                html.Div([
                                    html.Div([
                                        html.H4("CP-SAM Score"),
                                        html.P("96.03(-1.05)"),
                                    ], className="four columns graph-box"),
                                    html.Div([
                                        html.H4("Percentage of Load fed"),
                                        html.P("59.994(10.05)"),
                                    ], className="four columns graph-box"),
                                    html.Div([
                                        html.H4("Packet Loss Rate"),
                                        html.P("0.03(0.05)"),
                                    ], className="four columns graph-box"),
                                ], className="container"),

                                html.Div([
                                    html.H5("CP - SAM")

                                ], className="container graph-box-1"),

                                dcc.Graph(id="cp-graph", figure=fig_cp_sam)

                            ], className="six columns"),
                            html.Div(
                                [dcc.Graph(id="Graph_close",
                                           figure=fig)

                                 ], className="six columns"),

                        ], className="container"),

                    ], className="row map-box-row"),
                    html.Div([

                        dash_table.DataTable(id="anomaly-table-2",
                                             columns=[{"name": i, "id": i, "selectable": True} for i in
                                                      df_data.columns],
                                             row_selectable="multi",
                                             row_deletable=True,
                                             selected_rows=[],
                                             style_cell_conditional=[{
                                                 'if': {'column_id': c}, 'textAlign': 'left'} for c in
                                                 ['Date', 'Region']],
                                             style_data_conditional=[
                                                 {'if': {'row_index': 'odd'}, 'backgroundColor': 'rgb(248, 248, 248)'}],
                                             style_header={
                                                 'backgroundColor': 'rgb(230, 230, 230)',
                                                 'fontWeight': 'bold',
                                                 'text-align': 'center'
                                             }, page_size=6, page_action="native", data=df_data.to_dict('records'),
                                             selected_columns=["1", "2"]),

                    ], className="row table-box"),
                ]
            )
        ], className="page"
    )
