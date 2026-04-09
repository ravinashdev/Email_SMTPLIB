# ---------------------------- IMPORTS ------------------------------- #
import datetime as dt
# ---------------------------- CONSTANTS ------------------------------- #

# ---------------------------- GLOBAL VARIABLES ------------------------------- #

# ---------------------------- FUNCTIONS ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

today = dt.datetime.today()
year = today.year
month = today.month
day = today.day
day_of_week = today.weekday()
date_of_birth = dt.datetime(year=1990,month=9,day=10)

print(today)
print(year)
print(month)
print(day)
print(day_of_week)
print(date_of_birth)