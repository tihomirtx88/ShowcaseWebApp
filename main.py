import streamlit as st
import pandas

st.set_page_config(layout="wide");

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png");

with col2:
    st.title("Tihomir source");
    content = """
     Hi, I am Tihomir. I am Python and JavaScript programmer.
    """
    st.info(content)

df = pandas.read_csv("data.csv", sep=";");
col3, col4 = st.columns(2)

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"]);

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"]);

