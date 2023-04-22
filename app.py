import streamlit as st
import time
from commonutils import *

title_component(page_title = 'Environmental Monitoring System', layout = 'wide', initial_sidebar_state = 'auto')

sidebar_component(image = 'CSU.jpg')

tile_component = tile_components(['temperature_tile', 'humidity_tile', 'air_quality_tile', 'smoke_tile'])

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
        tile_component[0].metric("Temperature (C)", data_csv["field1"].iloc[-1] + " °C")
        tile_component[1].metric("Humidity (%)", data_csv["field2"].iloc[-1] + " %")
        tile_component[2].metric("Air Quality", data_csv["field3"].iloc[-1] + " PPM")
        tile_component[3].metric("Smoke", data_csv["field4"].iloc[-1] + " PPM")

# Run the main streamlit app loop
while True:
    update_data()
    time.sleep(15)
