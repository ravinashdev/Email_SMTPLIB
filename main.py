# ---------------------------- IMPORTS ------------------------------- #
import pandas as pd
import random
import datetime as dt
import os
import smtplib
# Use MIMEText instead to help construct better email
from email.mime.text import MIMEText
# Allows you to read the .env file
from dotenv import load_dotenv
# ---------------------------- PANDAS ------------------------------- #
motivational_quotes = pd.read_csv('Motivational Quotes.csv')
# print(motivational_quotes)
motivational_quotes_dictionary = motivational_quotes.iloc[:, 1:].to_dict('records')
# print(motivational_quotes_dictionary)
random_quote = random.choice(motivational_quotes_dictionary)
# print(random_quote)
# ---------------------------- CONSTANTS ------------------------------- #
load_dotenv()
# ---------------------------- GLOBAL VARIABLES ------------------------------- #
# To schedule a chron job on a server I'll use GitHub actions since it's free'
# ---------------------------- FUNCTIONS ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
now = dt.datetime.now()
weekday = now.weekday()

# Day of the week is Mon -> Fri
if weekday < 5:
    # Create initial connection
    body = f"'{random_quote["Quote"]}'\n-{random_quote["Author"]}"
    message = MIMEText(body)
    message['Subject'] = "Motivational Quote of The Day!"
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        # Start transport layer security
        connection.starttls()
        # Obscure username and password from GitHub public repo
        # Retrieve .env variables
        # -----------------------Local Setup------------------------
        # outgoing_email = os.getenv("SMTP_USER_OUTGOING_EMAIL")
        # outgoing_email_password = os.getenv("SMTP_USER_OUTGOING_EMAIL_APP_PASS")
        # receiving_email = os.getenv("SMTP_USER_RECEIVING_EMAIL")
        # -----------------------GitHub Actions Setup------------------------
        outgoing_email = os.environ.get("SMTP_USER_OUTGOING_EMAIL")
        outgoing_email_password = os.environ.get("SMTP_USER_OUTGOING_EMAIL_APP_PASS")
        receiving_email = os.environ.get("SMTP_USER_RECEIVING_EMAIL")
        connection.login(user=outgoing_email, password=outgoing_email_password)
        # Send the message with MIMEText
        connection.send_message(from_addr=outgoing_email, to_addrs=receiving_email, msg=message)