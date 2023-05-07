import streamlit as st # This is the main library, referred from https://streamlit.io/

def sidebar_component(csu_image, project_title, download_dataset_text, download_dataset_hyperlink):
    # using the image function from streamlit library.
    st.sidebar.image(csu_image)
    # using the title function from streamlit library.
    st.sidebar.title(project_title)
    # using the write function from streamlit library.
    st.sidebar.write(download_dataset_text)
    st.sidebar.write(download_dataset_hyperlink)
    return