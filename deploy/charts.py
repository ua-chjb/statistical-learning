import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

from data import uber_df1, uber_df3


############################# chart 0 ####################################
def figure0_timescatter():
    return px.scatter(uber_df1, y="reviewCreatedVersion", x="at", color_discrete_sequence=px.colors.qualitative.T10).update_layout({
        "title": "app versions over time"
    })

############################# chart 2 ####################################
def figure2_pie():
    return px.pie(uber_df1, "reviewCreatedVersion", color_discrete_sequence=px.colors.sequential.Teal[::-1]).update_traces({
        "textposition": "inside", "textinfo": "percent+label"
    }).update_layout({
        "title": "all app versions"
    })
############################# chart 3 ####################################
def figure3_scorehist(mask1):
    return px.histogram(uber_df3[mask1].sort_values(by="reviewCreatedVersion", ascending=True), x="score", color="reviewCreatedVersion", barmode="group", color_discrete_sequence=px.colors.qualitative.T10).update_layout({
        "title": "score by app version"
    })

############################# chart 4 ####################################
def figure4_stripthumbs(mask1):
    return px.strip(uber_df3[mask1].sort_values(by="reviewCreatedVersion", ascending=True), x="thumbsUpCount", color="reviewCreatedVersion", color_discrete_sequence= px.colors.qualitative.T10).update_layout({
        "title": """"thumbs up" by app version"""
    })

############################# chart 5 ####################################
def figure5_bubble(mask1):

    vr_gb2 = uber_df3[mask1].groupby(["reviewCreatedVersion"]).agg({"score": ["mean", "std"], "thumbsUpCount": ["mean", "std", "count"]}).reset_index()
    vr_gb2.columns = ["reviewCreatedVersion", "score_mean", "score_stdev", "thumbsUp_mean", "thumbsUp_stdev", "count"]

    return px.scatter(vr_gb2[mask1], x="score_mean", y="thumbsUp_mean", color="reviewCreatedVersion", size="count", color_discrete_sequence=px.colors.qualitative.T10).update_layout({
        "xaxis": {"range": [1, 5]}
    }).update_layout({
        "title": "score by thumbs up, view 1"
    })
############################# chart 7 ####################################
def table7_appversions():
    vr_gb2 = uber_df3.groupby(["reviewCreatedVersion"]).agg({"score": ["mean", "std"], "thumbsUpCount": ["mean", "std", "count"]}).reset_index()
    vr_gb2.columns = ["reviewCreatedVersion", "score_mean", "score_stdev", "thumbsUp_mean", "thumbsUp_stdev", "count"]
    for col in ["score_mean", "score_stdev", "thumbsUp_mean", "thumbsUp_stdev", "count"]:
        vr_gb2[col] = round(vr_gb2[col], 2)
    
    table7 = vr_gb2

    return table7
############################# chart 8 ####################################

def figure8_3d(mask1):
    return px.scatter_3d(
        uber_df3[mask1].sort_values(by="reviewCreatedVersion", ascending=True),
        x="score",
        y="reviewCreatedVersion",
        z="thumbsUpCount",
        color="reviewCreatedVersion",
        color_discrete_sequence=px.colors.qualitative.T10,
        opacity=0.5
    ).update_layout({
        "title": "score by thumbs up, view 2"
    })