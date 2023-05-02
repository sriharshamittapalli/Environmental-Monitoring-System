import altair as alt
import pandas as pd
import requests
import streamlit as st
import webbrowser

def title_component(page_title, layout, initial_sidebar_state): return st.set_page_config(page_title = page_title, layout = layout, initial_sidebar_state = initial_sidebar_state)

def open_support_ticket(): webbrowser.open("https://thingspeak.com/channels/2085717")

def sidebar_component():
    st.sidebar.image('CSU.png')
    st.sidebar.title('Environmental Monitoring System')
    return

def tile_components(tile_component_list):
    tile_component_list[0],tile_component_list[1],tile_component_list[2],tile_component_list[3] = st.columns(4)
    return tile_component_list[0].empty(), tile_component_list[1].empty(), tile_component_list[2].empty(), tile_component_list[3].empty()

# Define a function to fetch the latest data from ThingSpeak
def get_latest_data():
    url = "https://api.thingspeak.com/channels/2097821/feeds.json"
    response = requests.get(url)
    if response.status_code == 200: return pd.DataFrame(response.json()["feeds"])
    else: return pd.DataFrame()

def graph_component(data,type,title):
    data["Date"] = pd.to_datetime(data["created_at"])
    data[title] = data[type].astype(float)
    # define dynamic y-axis scale
    y_scale = alt.Scale(domain=(data[title].min() - 1, data[title].max() + 1))
    line = (alt.Chart(data[['Date', title]]).mark_line(color='blue').encode(alt.X("Date:T",title="Time"), alt.Y(title + ":Q",title=title, scale=y_scale), tooltip=["Date:T", title + ":Q"]).properties(title=title + " vs Time"))
    points = (alt.Chart(data[['Date', title]]).mark_point(color='red',size=30).encode(alt.X("Date:T",title="Time"), alt.Y(title + ":Q",title=title, scale=y_scale), tooltip=["Date:T", title + ":Q"]))
    chart = line + points
    st.altair_chart(chart,theme="streamlit",use_container_width=True)
