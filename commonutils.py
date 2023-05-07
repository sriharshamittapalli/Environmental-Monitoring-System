import altair as alt # This library used for graphs, referred from https://altair-viz.github.io/
import pandas as pd # This library is used for data, referred from https://pandas.pydata.org/
import requests # This library is used to get data from api, referred from https://pypi.org/project/requests/
import streamlit as st # This is the main library, referred from https://streamlit.io/
from datetime import datetime # This is used for timestamp conversions. referred from https://docs.python.org/3/library/datetime.html
import pytz # This is used for timezone conversions. referred from https://pypi.org/project/pytz/

def empty(variable):
    # using the empty function from streamlit library.
    return variable.empty()

def columns(number, tab = False):
    # using the columns function from streamlit library.
    if tab:
        return tab.columns(number)
    return st.columns(number)

def title_component(title_of_page, layout_of_page, sidebar_state):
    # using the set_page_config function from streamlit library.
    st.set_page_config(page_title = title_of_page,
                       layout = layout_of_page,
                       initial_sidebar_state = sidebar_state)
    return

def sidebar_component(csu_image, project_title, download_dataset_text, download_dataset_hyperlink):
    # using the image function from streamlit library.
    st.sidebar.image(csu_image)
    # using the title function from streamlit library.
    st.sidebar.title(project_title)
    # using the write function from streamlit library.
    st.sidebar.write(download_dataset_text)
    st.sidebar.write(download_dataset_hyperlink)
    return

def message_component(messages_list):
    messages_list[0], messages_list[1] = columns(len(messages_list))
    messages_list[0] = empty(messages_list[0])
    messages_list[1] = empty(messages_list[1])
    return messages_list[0], messages_list[1]

def tile_component(tiles_list):
    tiles_list[0],tiles_list[1],tiles_list[2],tiles_list[3] = columns(len(tiles_list))
    tiles_list[0] = empty(tiles_list[0])
    tiles_list[1] = empty(tiles_list[1])
    tiles_list[2] = empty(tiles_list[2])
    tiles_list[3] = empty(tiles_list[3])
    return tiles_list[0], tiles_list[1], tiles_list[2], tiles_list[3]

def tabs_component(tabs_list):
    # using the tabs function from streamlit library.
    tabs_list[0], tabs_list[1] = st.tabs(tabs_list)
    tabs_list[0] = empty(tabs_list[0])
    tabs_list[1] = empty(tabs_list[1])
    return tabs_list[0], tabs_list[1]

def graph_component(graphs_list, tab):
    graphs_list[0], graphs_list[1] = columns(len(graphs_list), tab)
    graphs_list[0] = empty(graphs_list[0])
    graphs_list[1] = empty(graphs_list[1])
    return graphs_list[0], graphs_list[1]

def metric_component(label, value, tile):
    # using the metrics function from streamlit library.
    tile.metric(label, value)

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

def logic_component(message_component_data, tile_component_data, tabs_component_data, tab1_graph_component, tab2_graph_component):
    # Get the latest data from ThingSpeak
    data_csv = get_latest_data()
    if not data_csv.empty:
        message_component_data[0].info(datetime.fromisoformat(data_csv["created_at"].iloc[-1][:-1]).replace(tzinfo=pytz.utc).astimezone(pytz.timezone('US/Eastern')).strftime("Last updated date at **%B %d, %Y** at **%I:%M:%S %p** EDT."), icon="ℹ️")
        # Implemented the metric_component function in commonutils.py file.
        metric_component("Temperature (C)", 
                        data_csv["field1"].iloc[-1] + " °F",
                        tile_component_data[0])
        metric_component("Humidity (%)",
                        data_csv["field2"].iloc[-1] + " %",
                        tile_component_data[1])
        metric_component("Air Quality",
                        data_csv["field3"].iloc[-1] + " PPM",
                        tile_component_data[2])
        metric_component("Smoke",
                        data_csv["field4"].iloc[-1] + " PPM",
                        tile_component_data[3])
        with tabs_component_data[0]:
            with tab1_graph_component[0]:
                line_graph_component(data_csv[["created_at", "field1"]].copy(deep=True),
                                    "field1",
                                    "Temperature")
            with tab1_graph_component[1]:
                line_graph_component(data_csv[["created_at", "field2"]].copy(deep=True),
                                    "field2",
                                    "Humidity")
        with tabs_component_data[1]:
            with tab2_graph_component[0]:
                line_graph_component(data_csv[["created_at", "field3"]].copy(deep=True),
                                    "field3",
                                    "Air Quality")
            with tab2_graph_component[1]:
                line_graph_component(data_csv[["created_at", "field4"]].copy(deep=True),
                                    "field4",
                                    "Smoke")
        if int(float(data_csv["field4"].iloc[-1])) > 400: message_component_data[1].warning(datetime.fromisoformat(data_csv["created_at"].iloc[-1][:-1]).replace(tzinfo=pytz.utc).astimezone(pytz.timezone('US/Eastern')).strftime("Smoke detected at **%B %d, %Y** at **%I:%M:%S %p** EDT."), icon="⚠️")
