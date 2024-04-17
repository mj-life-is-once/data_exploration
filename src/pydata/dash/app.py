import os

import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, callback, dcc, html


class DashReport:
    def __init__(self, output_dir=os.path.join(os.getcwd(), "data/output")):
        self.app = Dash(__name__)
        self.output_dir = output_dir
        df = pd.read_csv(
            "https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv"
        )
        self.app.layout = html.Div(
            [
                html.H1(children="Title of Dash App", style={"textAlign": "center"}),
                dcc.Dropdown(df.country.unique(), "Canada", id="dropdown-selection"),
                dcc.Graph(id="graph-content"),
            ]
        )

        @callback(
            Output("graph-content", "figure"), Input("dropdown-selection", "value")
        )
        def update_graph(value):
            dff = df[df.country == value]
            return px.line(dff, x="year", y="pop")
