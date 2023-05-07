# This is the main library, referred from https://streamlit.io/
import streamlit as st

def sidebar_component(csu_image, project_title, download_dataset_text, download_dataset_hyperlink):
    if csu_image:
        # using the image function from streamlit library.
        st.sidebar.image(csu_image)
    if project_title:
        # using the title function from streamlit library.
        st.sidebar.title(project_title)
    if download_dataset_text:
        # using the write function from streamlit library.
        st.sidebar.write(download_dataset_text)
    if download_dataset_hyperlink:
        st.sidebar.write(download_dataset_hyperlink)
    return
