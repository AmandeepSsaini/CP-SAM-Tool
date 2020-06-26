import dash_html_components as html
import dash_core_components as dcc
import random
import plotly
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()],className="main-header")


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.Div([
                        html.H6("CP-SAM Tool(Cyber-Physical Security Assessment Metric)")
                    ],className="six columns main-title"),
                    html.Div(
                        [
                            dcc.Link(
                                "Help",
                                href="/cp-sam-tool/full-view",
                                className="full-view-link",
                            )
                        ],
                        className="five columns",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="main-eader-top",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "CYBER-PHYSICAL",
                href="/cp-sam-tool/overview",
                className="tab first",
            ),
            dcc.Link(
                "PHYSICAL",
                href="/cp-sam-tool/physical",
                className="tab",
            ),
            dcc.Link(
                "CYBER",
                href="/cp-sam-tool/cyber",
                className="tab",
            ),
            dcc.Link(
                "EVENT", href="/cp-sam-tool/event", className="tab"
            ),
        ],
        className="all-tabs",
    )
    return menu

