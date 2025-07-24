import smtplib, ssl;
from dotenv import load_dotenv;
import os;

load_dotenv();

host = "smtp.gmail.com";
port = 465;

gmail_account = "tihomirtx88@gmail.com";
password = os.getenv("EMAIL_PASSWORD")

reciver = "tihomirtx88@gmail.com";

context = ssl.create_default_context();

message = """\
Subject: Test Email

Hi,
How are you,
Bye
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(gmail_account, password);
    server.sendmail(gmail_account, reciver, message)