from os import write

import streamlit as st
import pandas

st.set_page_config(layout="wide");

st.markdown("""
    <style>
        .main-title {
            color: #2c3e50;
            font-size: 36px;
            font-weight: bold;
        }
        .custom-header {
            color: #e74c3c;
            font-size: 22px;
            font-weight: 600;
            margin-bottom: 5px;
        }
        .description-text {
            font-size: 16px;
            color: #34495e;
            margin-bottom: 10px;
        }
        .source-link a {
            text-decoration: none;
            color: #2980b9;
            font-weight: bold;
        }
        img {
            border-radius: 10px;
            transition: transform 0.3s ease;
            margin-bottom: 10px;
        }
        img:hover {
            transform: scale(1.03);
        }
    </style>
""", unsafe_allow_html=True)



col1, col2 = st.columns(2)

with col1:
    st.image("photo2.jpg", width=250);

with col2:
    st.markdown("<div class='main-title'>Tihomir Source</div>", unsafe_allow_html=True)
    st.info("Hi, I am Tihomir. I am a Python and JavaScript programmer.")

df = pandas.read_csv("data.csv", sep=";");
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.markdown(f"<div class='custom-header'>{row['title']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='description-text'>{row['description']}</div>", unsafe_allow_html=True)
        st.image("images/" + row["image"], width=250)
        st.markdown(f"<div class='source-link'>[Source Code]({row['url']})</div>", unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)
        # st.write(f"[Open Project]({row['custom_url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.markdown(f"<div class='custom-header'>{row['title']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='description-text'>{row['description']}</div>", unsafe_allow_html=True)
        st.image("images/" + row["image"], width=250)
        st.markdown(f"<div class='source-link'>[Source Code]({row['url']})</div>", unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)
