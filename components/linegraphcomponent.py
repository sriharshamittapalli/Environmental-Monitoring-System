import altair as alt # This library used for graphs, referred from https://altair-viz.github.io/
import pandas as pd # This library is used for data, referred from https://pandas.pydata.org/
import streamlit as st # This is the main library, referred from https://streamlit.io/

def line_graph_component(data,type,title):
    data["Date"] = pd.to_datetime(data["created_at"])
    data[title] = data[type].astype(float)
    # define dynamic y-axis scale
    y_scale = alt.Scale(domain=(data[title].min() - 1, data[title].max() + 1))
    line = (alt.Chart(data[['Date', title]]).mark_line(color='blue').encode(alt.X("Date:T",title="Time"), alt.Y(title + ":Q",title=title, scale=y_scale), tooltip=["Date:T", title + ":Q"]).properties(title=title + " vs Time"))
    points = (alt.Chart(data[['Date', title]]).mark_point(color='red',size=30).encode(alt.X("Date:T",title="Time"), alt.Y(title + ":Q",title=title, scale=y_scale), tooltip=["Date:T", title + ":Q"]))
    chart = line + points
    st.altair_chart(chart,theme="streamlit",use_container_width=True)
