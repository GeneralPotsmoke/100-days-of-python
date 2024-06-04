import smtplib
import pandas as pd
import datetime as dt
import random

MY_EMAIL = "your_email@example.com"
MY_PASSWORD = "your_password"

# Reading the CSV file
birthdays = pd.read_csv("birthdays.csv")

# Checking if today matches a birthday
today = (dt.datetime.now().month, dt.datetime.now().day)
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthdays.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.example.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!

{contents}"
        )
