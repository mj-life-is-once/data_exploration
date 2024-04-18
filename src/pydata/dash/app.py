import os

import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, callback, dcc, html

from pydata import Importer


class DashReport:
    def __init__(self, output_dir=os.path.join(os.getcwd(), "data/output")):
        self.app = Dash(__name__)
        self.output_dir = output_dir
        self.df = self.importData()
        self.app.layout = html.Div(
            [
                html.Link(rel="stylesheet", href="/assets/style.css"),
                html.H1(children="Title of Dash App", style={"textAlign": "center"}),
                dcc.Dropdown(
                    self.df.country.unique(),
                    "Canada",
                    id="dropdown-selection",
                ),
                dcc.Graph(id="graph-content"),
            ]
        )

        @callback(
            Output("graph-content", "figure"), Input("dropdown-selection", "value")
        )
        def update_graph(value):
            dff = self.df[self.df.country == value]
            fig = px.line(dff, x="year", y="pop")
            fig.update_layout(
                template="plotly_dark",
            )
            return fig

    def importData(self):
        df = pd.read_csv(
            "https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv"
        )
        return df
