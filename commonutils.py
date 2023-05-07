import pandas as pd # This library is used for data, referred from https://pandas.pydata.org/
import requests # This library is used to get data from api, referred from https://pypi.org/project/requests/
import streamlit as st # This is the main library, referred from https://streamlit.io/

def empty(variable):
    # using the empty function from streamlit library.
    return variable.empty()

def columns(number, tab = False):
    if tab:
        return tab.columns(number) # using the columns function from streamlit library.
    else:
        return st.columns(number) # using the columns function from streamlit library.

# Define a function to fetch the latest data from ThingSpeak
def get_latest_data():
    channel_feed = "https://api.thingspeak.com/channels/2097821/feeds.json"
    json_response = requests.get(channel_feed)  # using the get function from requests library.
    if json_response.status_code == 200: # getting status as 200 means success.
        return pd.DataFrame(json_response.json()["feeds"]) # using the DataFrame function from pandas library.
    else:
        return pd.DataFrame() # using the DataFrame function from pandas library.
