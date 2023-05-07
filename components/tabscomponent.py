import streamlit as st # This is the main library, referred from https://streamlit.io/
from commonutils import *

def tabs_component(tabs_list):
    # using the tabs function from streamlit library.
    tabs_list[0], tabs_list[1] = st.tabs(tabs_list)
    tabs_list[0] = empty(tabs_list[0])
    tabs_list[1] = empty(tabs_list[1])
    return tabs_list[0], tabs_list[1]