import streamlit as st
import pandas as pd
import time
import requests
from commonutils import *

# Define a function to fetch the latest data from ThingSpeak
def get_latest_data():
    url = "https://api.thingspeak.com/channels/2085717/feeds.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data["feeds"])
    else:
        return pd.DataFrame()

page_styles(page_title = 'Environmental Monitoring System', layout = 'wide', initial_sidebar_state = 'auto')

with st.sidebar: st.image("CSU.jpg")

temperature_tile, humidity_tile, air_quality_tile, smoke_tile = st.columns(4)
temperature_tile = temperature_tile.empty()
humidity_tile = humidity_tile.empty()
air_quality_tile = air_quality_tile.empty()
smoke_tile = smoke_tile.empty()

temperature_humidity_graph_tab,air_quality_smoke_graph_tab = st.tabs(["Temperature and Humidity","Air Quality and Smoke / Gas"])
temperature_humidity_graph_tab = temperature_humidity_graph_tab.empty()
air_quality_smoke_graph_tab = air_quality_smoke_graph_tab.empty()

temperature_graph, humidity_graph= temperature_humidity_graph_tab.columns(2)
temperature_graph = temperature_graph.empty()
humidity_graph = humidity_graph.empty()

air_quality_graph, smoke_graph= air_quality_smoke_graph_tab.columns(2)
air_quality_graph = air_quality_graph.empty()
smoke_graph = smoke_graph.empty()

# smoke_detected = st.sidebar.empty()

def update_data():
    # Get the latest data from ThingSpeak
    data_csv = get_latest_data()
    if not data_csv.empty:
        with temperature_humidity_graph_tab:
            with temperature_graph: graph_component(data_csv[["created_at", "field1"]].copy(deep=True),"field1","Temperature")
            with humidity_graph: graph_component(data_csv[["created_at", "field2"]].copy(deep=True),"field2","Humidity")
        with air_quality_smoke_graph_tab:
            with air_quality_graph: graph_component(data_csv[["created_at", "field3"]].copy(deep=True),"field3","Air Quality")
            with smoke_graph: graph_component(data_csv[["created_at", "field4"]].copy(deep=True),"field4","Smoke")
        # Update the temperature, humidity, air quality, and smoke placeholders
        temperature_tile.metric("Temperature (C)", data_csv["field1"].iloc[-1] + " °C")
        humidity_tile.metric("Humidity (%)", data_csv["field2"].iloc[-1] + " %")
        air_quality_tile.metric("Air Quality", data_csv["field3"].iloc[-1] + " PPM")
        smoke_tile.metric("Smoke", data_csv["field4"].iloc[-1] + " PPM")

#         if int(data_csv["field4"].iloc[-1]) > 400:
#             smoke_detected.empty()
#             time.sleep(1)
#             smoke_detected.write("Smoke Detected")
#         else:
#             smoke_detected.empty()
#             time.sleep(1)
#             smoke_detected.write("No Smoke Detected")

# Run the main streamlit app loop
while True:
    update_data()
    time.sleep(15)
