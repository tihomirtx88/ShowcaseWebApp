import streamlit as st

st.header("Contact Us");

with st.form(key="email_form"):
    user_name = st.text_input("Your email address");
    message = st.text_area("Your message");
    button = st.form_submit_button("Submit");
    if button:
        print("Succes submit");