import altair as alt # This library used for graphs, referred from https://altair-viz.github.io/
import pandas as pd # This library is used for data, referred from https://pandas.pydata.org/
import streamlit as st # This is the main library, referred from https://streamlit.io/

def line_graph_component(data,type,title):
    # Learned how to design line graphs and points from https://altair-viz.github.io/
    data["Date"] = pd.to_datetime(data["created_at"]) # Using the to_datetime function from pandas.
    data[title] = data[type].astype(float)
    # Using Scale function from altair library.
    y_scale = alt.Scale(
                        domain = (
                                 data[title].min() - 1,
                                 data[title].max() + 1
                                 )
                        )
    line = (
           alt.Chart(data[["Date", title]]) # Using Chart function from altair library.
           .mark_line(color = "blue") # Marking the line color as blue. Using mark_line function from altair library.
            # Using the encode function from altair library.
           .encode(
                 alt.X(
                      "Date:T", # Formating date, also learned how to do these operations from https://altair-viz.github.io/
                      title = "Time"
                 ),
                 alt.Y(
                      title + ":Q", # Formating title, also learned how to do these operations from https://altair-viz.github.io/
                      title = title,
                      scale = y_scale
                 ),
                 tooltip=["Date:T", title + ":Q"])
            # Using the properties function from altair library.
           .properties(
                      title = title + " vs Time"
                      )
            )
    
    points = (
            alt.Chart(data[["Date", title]]) # Using Chart function from altair library.
            # Using mark_point function from altair library.
            .mark_point(
                       color = "red", # Marking the points color as red
                       size = 30
                       )
            # Using encode function from altair library.
            .encode(
                   alt.X(
                        "Date:T",
                        title = "Time"
                        ),
                   alt.Y(
                        title + ":Q",
                        title = title,
                        scale = y_scale
                        ),
                   tooltip=["Date:T", title + ":Q"]
                   )
            )
    # Using altair_chart function from streamlit library.
    st.altair_chart(
                    line + points,
                    theme = "streamlit",
                    use_container_width = True
                    )
