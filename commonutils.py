import altair as alt
import pandas as pd
import requests
import streamlit as st

def title_component(page_title, layout, initial_sidebar_state): return st.set_page_config(page_title = page_title, layout = layout, initial_sidebar_state = initial_sidebar_state)

def sidebar_component(image): return st.sidebar.image(image)

def get_data(url):
    response = requests.get(url)
    if response.status_code == 200: return response.json()
    else: return None

def get_feeds_data(data): return pd.DataFrame(data["feeds"])

def graph_component(data,type,title):
    data["Date"] = pd.to_datetime(data["created_at"])
    data[title] = data[type].astype(float)
    
    # define dynamic y-axis scale
    y_scale = alt.Scale(domain=(data[title].min() - 1, data[title].max() + 1))

    line = (
        alt.Chart(data[['Date', title]])
        .mark_line(color='blue')  # set line color
        .encode(
            alt.X("Date:T",title="Time"),
            alt.Y(title + ":Q",title=title, scale=y_scale),
            tooltip=["Date:T", title + ":Q"],
        )
        .properties(title=title + " vs Time")
    )

    points = (
        alt.Chart(data[['Date', title]])
        .mark_point(color='red',size=30)  # set point color
        .encode(
            alt.X("Date:T",title="Time"),
            alt.Y(title + ":Q",title=title, scale=y_scale),
            tooltip=["Date:T", title + ":Q"],
        )
    )

    chart = line + points

    st.altair_chart(chart,theme="streamlit")
