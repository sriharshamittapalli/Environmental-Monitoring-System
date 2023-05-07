# This is the main library, referred from https://streamlit.io/
import streamlit as st

def title_component(title_of_page, layout_of_page, sidebar_state):
    # using the set_page_config function from streamlit library.
    if title_of_page:
        if layout_of_page:
            if sidebar_state:
                st.set_page_config(page_title = title_of_page,
                                layout = layout_of_page,
                                initial_sidebar_state = sidebar_state)
    return
