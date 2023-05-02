import streamlit as st # This is the main library, referred from https://streamlit.io/
import time # This is used for updating the application every 15 seconds.
from commonutils import * # Created all important functions in commonutils which helps in re-using functions and code readaility
from datetime import datetime
import pytz

title_component(page_title = 'EMS Anytime', layout = 'wide', initial_sidebar_state = 'auto') # Created title component function in commonutils

sidebar_component() # Created sidebar component in commonutils

last_update_component,smoke_detected_component = st.columns(2)
smoke_detected_component = smoke_detected_component.empty()
last_update_component = last_update_component.empty()

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

tooltip_information = st.sidebar.empty()

download_dataset_button = st.sidebar.empty()

def update_data():
    # Get the latest data from ThingSpeak
    data_csv = get_latest_data()
    if not data_csv.empty:
        last_update_component.info(datetime.fromisoformat(data_csv["created_at"].iloc[-1][:-1]).replace(tzinfo=pytz.utc).astimezone(pytz.timezone('US/Eastern')).strftime("Last updated date at **%B %d, %Y** at **%I:%M:%S %p** EDT."), icon="ℹ️")
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
        if int(float(data_csv["field4"].iloc[-1])) > 100: smoke_detected_component.warning(datetime.fromisoformat(data_csv["created_at"].iloc[-1][:-1]).replace(tzinfo=pytz.utc).astimezone(pytz.timezone('US/Eastern')).strftime("Smoke detected at **%B %d, %Y** at **%I:%M:%S %p** EDT."), icon="⚠️")
        tooltip_information.write("Click on the option below to download the data, which will redirect you to ThingSpeak. Then click the **Export recent data** button to download the dataset.")
        if download_dataset_button.button("Download Dataset", on_click=open_support_ticket, key=button_key): st.experimental_rerun()

counter = 0

while True:
    counter += 1
    button_key = f"button_{counter}"
    update_data() # Get the latest data from thingspeak server.
    time.sleep(15) # Update the application every 15 seconds. Referred from https://www.pythoncentral.io/how-to-add-time-delay-in-your-python-code/
