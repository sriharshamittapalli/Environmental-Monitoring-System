from commonutils import * # Created all important functions in commonutils which helps in re-using functions and code readability
from datetime import datetime # This is used for timestamp conversions. referred from https://docs.python.org/3/library/datetime.html
import pytz # This is used for timezone conversions. referred from https://pypi.org/project/pytz/
from components import metriccomponent

def logic_component(message_component_data, tile_component_data, tabs_component_data, tab1_graph_component, tab2_graph_component):
    # Get the latest data from ThingSpeak
    data_csv = get_latest_data()
    if not data_csv.empty:
        message_component_data[0].info(datetime.fromisoformat(data_csv["created_at"].iloc[-1][:-1]).replace(tzinfo=pytz.utc).astimezone(pytz.timezone('US/Eastern')).strftime("Last updated date at **%B %d, %Y** at **%I:%M:%S %p** EDT."), icon="ℹ️")
        # Implemented the metric_component function in commonutils.py file.
        metriccomponent.metric_component("Temperature (C)",
                        data_csv["field1"].iloc[-1] + " °F",
                        tile_component_data[0])
        metriccomponent.metric_component("Humidity (%)",
                        data_csv["field2"].iloc[-1] + " %",
                        tile_component_data[1])
        metriccomponent.metric_component("Air Quality",
                        data_csv["field3"].iloc[-1] + " PPM",
                        tile_component_data[2])
        metriccomponent.metric_component("Smoke",
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
