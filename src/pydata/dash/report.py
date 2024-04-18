import pandas as pd
import plotly.graph_objs as go
from dash import Dash, Input, Output, callback, dcc, html
from dash_bootstrap_templates import load_figure_template

from .visualiser import AllUser, SingleUser


class Report:
    @staticmethod
    def all_report(ev_data: pd.DataFrame):
        return html.Div(
            className="report",
            # style={"paddig": "10px", "margin": "10px"},
            children=[
                dcc.Graph(
                    figure=AllUser.distace_histogram(ev_data, "Distance Histogram"),
                    className="col s12 m6",
                ),
                dcc.Graph(
                    figure=AllUser.facility_pie_chart(ev_data, "Facility Pie Chart"),
                    className="col s12 m6",
                ),
            ],
        )

    @staticmethod
    def single_user_report(ev_data: pd.DataFrame, userId: str):

        ev_data_user = ev_data[ev_data["userId"] == int(userId)]
        # print("sigle user report", ev_data_user, userId)
        return html.Div(
            className="report",
            children=[
                dcc.Graph(
                    figure=SingleUser.heatmap(ev_data_user, f"Heatmap: {userId}"),
                    className="col s12 m6",
                ),
                dcc.Graph(
                    figure=SingleUser.heatmap_with_duration(
                        ev_data_user, f"Heatmap with Duration: {userId}"
                    ),
                    className="col s12 m6",
                ),
            ],
        )
