from smtplib import *
import random as rnd
import pandas as pd
import datetime as dt

data = pd.read_csv("birthdays.csv")
current_date = dt.datetime.now()

for index, row in data.iterrows():
    if row["year"] == current_date.year and row["month"] == current_date.month and row["day"] == current_date.day:
        random_number = rnd.randint(1, 3)
        with open(f"./letter_templates/letter_{random_number}.txt") as file:
            letter = file.read()
        letter = letter.replace("[NAME]", f"{row['name']}")
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="antonios.saliba1@gmail.com", password="girgllhuentjkgty")
            connection.sendmail(from_addr="antonios.saliba1@gmail.com", to_addrs=f"{row['email']}", msg=f"Subject:Happy Birthday!\n\n{letter}")