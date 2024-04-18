import os

import numpy as np
import pandas as pd

# Plotly
import plotly.express as px
import plotly.graph_objs as go
import plotly.io as pio
from plotly.subplots import make_subplots

from pydata import Transformer


class Visualiser:
    FONT_S = dict(family="Courier New, monospace", size=8)
    FONT_M = dict(family="Courier New, monospace", size=12)
    FONT_L = dict(family="Courier New, monospace", size=24)

    WIDTH_S = 600
    WIDTH_M = 800
    WIDTH_L = 1200
    THEME = "dark"  # dark or light

    tabs_styles = {
        "flex-direction": "row",
    }
    tab_style = {
        "color": "#AEAEAE",
        "backgroundColor": "#181414",
    }

    tab_selected_style = {
        "fontWeight": "bold",
        "color": "#ffffff",
        "backgroundColor": "#5665c7",
    }


class SingleUser:

    @staticmethod
    def heatmap(df: pd.DataFrame, title: str, theme="dark") -> go.Figure:
        draw_df = df.copy()
        draw_df = Transformer.sort_by_week(df)
        fig = go.Figure(
            data=go.Histogram2d(
                x=draw_df["startTime"],
                y=draw_df["weekday"],
                xbins=dict(start=0, end=24, size=round(1, 1)),
                nbinsy=7,
                colorscale="ice",
            )
        )

        fig.update_layout(
            title={
                "text": title,
                "y": 0.9,
                "x": 0.5,
                "xanchor": "center",
                "yanchor": "top",
            },
            template="plotly_dark" if theme == "dark" else "plotly_white",
            font=Visualiser.FONT_M,
        )
        return fig

    def heatmap_with_duration(df: pd.DataFrame, title: str, theme="dark") -> go.Figure:
        draw_df = df.copy()
        draw_df = Transformer.sort_by_week(df)
        fig = go.Figure(
            go.Heatmap(
                z=draw_df["chargeTimeHrs"],
                x=draw_df["startTime"],
                y=draw_df["weekday"],
                coloraxis="coloraxis",
            )
        )
        fig.update_layout(
            title={
                "text": title,
                "y": 0.9,
                "x": 0.5,
                "xanchor": "center",
                "yanchor": "top",
            },
            template="plotly_dark" if theme == "dark" else "plotly_white",
            font=Visualiser.FONT_M,
        )
        return fig


class AllUser:
    @staticmethod
    def distace_histogram(df: pd.DataFrame, title: str, theme="dark") -> go.Figure:
        ev_data = df.copy()
        ev_data_distance = ev_data[ev_data["distance"].notna()]
        ev_data_distance["distance(mi)"] = ev_data_distance["distance"].astype(float)
        ev_data_distance["distance(km)"] = ev_data_distance["distance(mi)"] * 1.60934
        fig = go.Figure(
            data=[go.Histogram(y=ev_data_distance["distance(km)"], nbinsx=10)]
        )
        fig.update_layout(
            title={
                "text": title,
                "y": 0.9,
                "x": 0.5,
                "xanchor": "center",
                "yanchor": "top",
            },
            font=Visualiser.FONT_M,
            template="plotly_dark" if theme == "dark" else "plotly_white",
        )
        fig.update_yaxes(title_text="Distance(km)")
        fig.update_xaxes(title_text="Count")
        return fig

    def facility_pie_chart(
        ev_data: pd.DataFrame, title: str, theme="dark"
    ) -> go.Figure:
        facility_types = [
            "manufacturing",
            "office",
            "research and \ndevelopment",
            "other",
        ]
        fig = go.Figure(
            data=[
                go.Pie(
                    labels=facility_types,
                    values=ev_data["facilityType"].value_counts(),
                    hole=0.3,
                )
            ]
        )
        fig.update_layout(
            title={
                "text": title,
                "y": 0.9,
                "x": 0.5,
                "xanchor": "center",
                "yanchor": "top",
            },
            font=Visualiser.FONT_M,
            template="plotly_dark" if theme == "dark" else "plotly_white",
        )
        return fig
