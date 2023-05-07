import altair as alt # This library used for graphs, referred from https://altair-viz.github.io/
import pandas as pd # This library is used for data, referred from https://pandas.pydata.org/
import requests # This library is used to get data from api, referred from https://pypi.org/project/requests/
import streamlit as st # This is the main library, referred from https://streamlit.io/

def empty(variable):
    # using the empty function from streamlit library.
    return variable.empty()

def columns(number, tab = False):
    # using the columns function from streamlit library.
    if tab:
        return tab.columns(number)
    return st.columns(number)

# Define a function to fetch the latest data from ThingSpeak
def get_latest_data():
    channel_feed = "https://api.thingspeak.com/channels/2097821/feeds.json"
    # using the get function from requests library.
    response = requests.get(channel_feed)
    if response.status_code == 200:
        return pd.DataFrame(response.json()["feeds"]) # using the dataframe function from requests library.
    else:
        return pd.DataFrame()

def line_graph_component(data,type,title):
    data["Date"] = pd.to_datetime(data["created_at"])
    data[title] = data[type].astype(float)
    # define dynamic y-axis scale
    y_scale = alt.Scale(domain=(data[title].min() - 1, data[title].max() + 1))
    line = (alt.Chart(data[['Date', title]]).mark_line(color='blue').encode(alt.X("Date:T",title="Time"), alt.Y(title + ":Q",title=title, scale=y_scale), tooltip=["Date:T", title + ":Q"]).properties(title=title + " vs Time"))
    points = (alt.Chart(data[['Date', title]]).mark_point(color='red',size=30).encode(alt.X("Date:T",title="Time"), alt.Y(title + ":Q",title=title, scale=y_scale), tooltip=["Date:T", title + ":Q"]))
    chart = line + points
    st.altair_chart(chart,theme="streamlit",use_container_width=True)

