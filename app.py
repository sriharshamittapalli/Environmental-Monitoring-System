import time # This is used for updating the application every 15 seconds. Mainly used for delay, referred from https://docs.python.org/3/library/time.html
from commonutils import * # Implemented all important functions in commonutils.
# Implemented all important sub parts in components which helps in re-using functions and code readability.
from components import titlecomponent
from components import sidebarcomponent
from components import messagecomponent
from components import tilecomponent
from components import tabscomponent
from components import graphcomponent
from components import logiccomponent

# Implemented the title_component function in titlecomponent.py file.
# In the title_component, we are displaying EMS Anytime as title of the page.
# Setting layout as wide such that UI looks good.
# Showing sidebar as default whenever we open the application.
titlecomponent.title_component(title_of_page = "EMS Anytime",
                layout_of_page = "wide",
                sidebar_state = "auto"
                )

# Implemented the sidebar_component function in sidebarcomponent.py file.
# In the sidebar_component, we are displaying CSU logo. downloaded from https://www.csuohio.edu/marketing/logos
# Displaying the title in sidebar as "Environmental Monitoring System".
# Displaying the information about how to download the data from ThingSpeak.
# Showing a hyperlink which redirects to ThingSpeak where we can download the data. https://thingspeak.com/channels/2097821
sidebarcomponent.sidebar_component(csu_image = "images/CSU.png",
                  project_title = "Environmental Monitoring System",
                  download_dataset_text = "Click on the hyperlink below to download the data, which will redirect you to ThingSpeak. Then click the Export recent data button to download the dataset.",
                  download_dataset_hyperlink = "[Download Dataset](https://thingspeak.com/channels/2097821)"
                  )

messages_list = []
# we are just appending values to the list.
messages_list.append("last_update_component")
messages_list.append("smoke_detected_component")
message_component_data = messagecomponent.message_component(messages_list) # Implemented the message_components function in messagecomponent.py file.

tiles_list = []
# we are just appending values to the list.
tiles_list.append("temperature_tile")
tiles_list.append("humidity_tile")
tiles_list.append("air_quality_tile")
tiles_list.append("smoke_tile")
tile_component_data = tilecomponent.tile_component(tiles_list) # Implemented the tile_components function in tilecomponent.py file.

tabs_list = []
# we are just appending values to the list.
tabs_list.append("Temperature and Humidity")
tabs_list.append("Air Quality and Smoke / Gas")
tabs_component_data = tabscomponent.tabs_component(tabs_list) # Implemented the tabs_components function in tabscomponent.py file.

tab1_graphs_list = []
# we are just appending values to the list.
tab1_graphs_list.append("temperature_graph")
tab1_graphs_list.append("humidity_graph")
tab1_graph_component = graphcomponent.graph_component(tab1_graphs_list, tabs_component_data[0]) # Implemented the graph_components function in graphcomponent.py file.

tab2_graphs_list = []
# we are just appending values to the list.
tab2_graphs_list.append("air_quality_graph")
tab2_graphs_list.append("smoke_graph")
tab2_graph_component = graphcomponent.graph_component(tab2_graphs_list, tabs_component_data[1]) # Implemented the graph_components function in graphcomponent.py file.

while True:
    # Implemented the logic_component function in logiccomponent.py file.
    logiccomponent.logic_component(message_component_data,
                   tile_component_data,
                   tabs_component_data,
                   tab1_graph_component,
                   tab2_graph_component) 
    time.sleep(15) # Utilized the sleep function from time package. Updating the application every 15 seconds.
