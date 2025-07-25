import streamlit as st
from send_email import send_email

st.header("Contact Us");

with st.form(key="email_form"):
    user_name = st.text_input("Your email address");
    raw_message = st.text_area("Your message");
    message = f"""\
    Subject: New message from {user_name}

    You received a new message from your contact form:

    From: {user_name}
    Message:
    {raw_message}
    """
    button = st.form_submit_button("Submit");
    if button:
        send_email(message, receiver= user_name);
        st.info("Your email sent success");