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
    else:
        return st.columns(number)

# Define a function to fetch the latest data from ThingSpeak
def get_latest_data():
    channel_feed = "https://api.thingspeak.com/channels/2097821/feeds.json"
    # using the get function from requests library.
    json_response = requests.get(channel_feed)
    if json_response.status_code == 200:
        return pd.DataFrame(json_response.json()["feeds"]) # using the dataframe function from requests library.
    else:
        return pd.DataFrame()
