import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pages import (
    overview,
    Physical,
    Cyber,
    Event,
    Strategy,
    Help,
)

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/cp-sam-tool/physical":
        return Physical.create_layout(app)
    elif pathname == "/cp-sam-tool/cyber":
        return Cyber.create_layout(app)
    elif pathname == "/cp-sam-tool/event":
        return Event.create_layout(app)
    elif pathname == "/cp-sam-tool/strategy":
        return Strategy.create_layout(app)
    elif pathname == "/cp-sam-tool/help":
        return Help.create_layout(app)
    elif pathname == "/cp-sam-tool/full-view":
        return (
            overview.create_layout(app),
            Physical.create_layout(app),
            Cyber.create_layout(app),
            Event.create_layout(app),
            Strategy.create_layout(app),
            Help.create_layout(app),
        )
    else:
        return overview.create_layout(app)


if __name__ == "__main__":
    app.run_server(debug=True)
