import os

import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, callback, dcc, html

from pydata import Importer, Transformer

from .report import Report
from .visualiser import Visualiser


class DashReport:
    def __init__(self, import_dir=os.path.join(os.getcwd(), "data")):
        self.app = Dash(__name__)
        self.import_dir = import_dir
        self.df = self.importData()
        self.df = self.transformData()
        self.app.layout = html.Div(
            [
                html.Link(rel="stylesheet", href="/assets/style.css"),
                html.H1(
                    children="Sample Dash App",
                    className="dash-title",
                ),
                dcc.Tabs(
                    id="tabs-with-classes",
                    value="all",
                    parent_className="custom-tabs",
                    className="custom-tabs-container",
                    children=[
                        dcc.Tab(
                            label="All Users",
                            value="all",
                            className="custom-tab",
                            style=Visualiser.tab_style,
                            selected_className="custom-tab--selected",
                            selected_style=Visualiser.tab_selected_style,
                        ),
                        dcc.Tab(
                            label="Singer User",
                            value="single",
                            className="custom-tab",
                            style=Visualiser.tab_style,
                            selected_className="custom-tab--selected",
                            selected_style=Visualiser.tab_selected_style,
                        ),
                    ],
                ),
                html.Div(id="tabs-content-classes"),
            ]
        )

        @callback(
            Output("tabs-content-classes", "children"),
            Input("tabs-with-classes", "value"),
        )
        def render_content(tab):
            if tab == "single":
                return Report.single_user_report(self.df, "35897499")

            if tab == "all":
                return Report.all_report(self.df)

    def importData(self):
        return Importer.read_csv(
            os.path.join(self.import_dir, "cleaned_ev_charge_data.csv"),
        )

    def transformData(self):
        return Transformer.reformat_datetime(self.df)
