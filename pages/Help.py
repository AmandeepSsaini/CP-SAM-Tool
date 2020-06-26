import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from utils import Header
import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()





def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 2
        ],
        className="page",
    )
