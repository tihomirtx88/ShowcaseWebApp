from os import write

import streamlit as st
import pandas

st.set_page_config(layout="wide");

col1, col2 = st.columns(2)

with col1:
    st.image("photo2.jpg");

with col2:
    st.title("Tihomir source");
    content = """
     Hi, I am Tihomir. I am Python and JavaScript programmer.
    """
    st.info(content)

df = pandas.read_csv("data.csv", sep=";");
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"]);
        st.write(row["description"]);
        st.image("images/" + row["image"]);
        st.write(f"[Source Code]({row['url']})");
        # st.write(f"[Open Project]({row['custom_url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"]);
        st.write(row["description"]);
        st.image("images/" + row["image"]);

