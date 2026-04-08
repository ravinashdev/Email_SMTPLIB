# ---------------------------- IMPORTS ------------------------------- #
import os
import smtplib
from dotenv import load_dotenv
# ---------------------------- CONSTANTS ------------------------------- #

# ---------------------------- GLOBAL VARIABLES ------------------------------- #

# ---------------------------- FUNCTIONS ------------------------------- #
load_dotenv()
# ---------------------------- UI SETUP ------------------------------- #

# Create initial connection
connection = smtplib.SMTP('smtp.gmail.com', 587)
# Start transport layer security
connection.starttls()
# Obscure username and password from GitHub public repo
# Retrieve .env variables
outgoing_email = os.getenv("SMTP_USER_OUTGOING_EMAIL")
outgoing_email_password = os.getenv("SMTP_USER_OUTGOING_EMAIL_APP_PASS")
receiving_email = os.getenv("SMTP_USER_RECEIVING_EMAIL")
connection.login(user=outgoing_email, password=outgoing_email_password)
# Send message
message = f"Hello Ryan this a test of the smtplib in python"
connection.sendmail(from_addr=outgoing_email, to_addrs=receiving_email, msg=message)
connection.close()