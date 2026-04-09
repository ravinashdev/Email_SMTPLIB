# ---------------------------- IMPORTS ------------------------------- #
import os
import smtplib
# Allows you to read the .env file
from dotenv import load_dotenv
# ---------------------------- CONSTANTS ------------------------------- #

# ---------------------------- GLOBAL VARIABLES ------------------------------- #

# ---------------------------- FUNCTIONS ------------------------------- #
# Loads .env file contents
load_dotenv()
# ---------------------------- UI SETUP ------------------------------- #

# Create initial connection
with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    # Start transport layer security
    connection.starttls()
    # Obscure username and password from GitHub public repo
    # Retrieve .env variables
    outgoing_email = os.getenv("SMTP_USER_OUTGOING_EMAIL")
    outgoing_email_password = os.getenv("SMTP_USER_OUTGOING_EMAIL_APP_PASS")
    receiving_email = os.getenv("SMTP_USER_RECEIVING_EMAIL")
    connection.login(user=outgoing_email, password=outgoing_email_password)
    # Send message
    message = f"Subject: Email_SMTPLIB_TEST\n\n Hello Ryan, \n\nThis a test of the smtplib in python with a subject"
    connection.sendmail(from_addr=outgoing_email, to_addrs=receiving_email, msg=message)