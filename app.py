import streamlit as st # This is the main library, referred from https://streamlit.io/
import time # This is used for updating the application every 15 seconds.
from commonutils import * # Created all important functions in commonutils which helps in re-using functions and code readaility

title_component(page_title = 'EMS Anytime', layout = 'wide', initial_sidebar_state = 'auto') # Created title component function in commonutils

sidebar_component() # Created sidebar component in commonutils

tile_component = tile_components(['temperature_tile', 'humidity_tile', 'air_quality_tile', 'smoke_tile']) # Created tiles in commonutils

temperature_humidity_graph_tab,air_quality_smoke_graph_tab = st.tabs(["Temperature and Humidity","Air Quality and Smoke / Gas"])
temperature_humidity_graph_tab = temperature_humidity_graph_tab.empty()
air_quality_smoke_graph_tab = air_quality_smoke_graph_tab.empty()

temperature_graph, humidity_graph= temperature_humidity_graph_tab.columns(2)
temperature_graph = temperature_graph.empty()
humidity_graph = humidity_graph.empty()

air_quality_graph, smoke_graph= air_quality_smoke_graph_tab.columns(2)
air_quality_graph = air_quality_graph.empty()
smoke_graph = smoke_graph.empty()

def update_data():
    # Get the latest data from ThingSpeak
    data_csv = get_latest_data()
    if not data_csv.empty:
        tile_component[0].metric("Temperature (C)", data_csv["field1"].iloc[-1] + " °F")
        tile_component[1].metric("Humidity (%)", data_csv["field2"].iloc[-1] + " %")
        tile_component[2].metric("Air Quality", data_csv["field3"].iloc[-1] + " PPM")
        tile_component[3].metric("Smoke", data_csv["field4"].iloc[-1] + " PPM")
        with temperature_humidity_graph_tab:
            with temperature_graph: graph_component(data_csv[["created_at", "field1"]].copy(deep=True),"field1","Temperature")
            with humidity_graph: graph_component(data_csv[["created_at", "field2"]].copy(deep=True),"field2","Humidity")
        with air_quality_smoke_graph_tab:
            with air_quality_graph: graph_component(data_csv[["created_at", "field3"]].copy(deep=True),"field3","Air Quality")
            with smoke_graph: graph_component(data_csv[["created_at", "field4"]].copy(deep=True),"field4","Smoke")

while True:
    update_data() # Get the latest data from thingspeak server.
    time.sleep(15) # Update the application every 15 seconds. Referred from https://www.pythoncentral.io/how-to-add-time-delay-in-your-python-code/
