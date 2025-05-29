from smtplib import *
import random as rnd
import datetime as dt

current_day = dt.datetime.now().weekday()
if current_day == 3:
    list_of_quotes = []
    with open("quotes.txt") as file:
        for line in file:
            list_of_quotes.append(line)
    random_quote = list_of_quotes[rnd.randint(0, len(list_of_quotes) - 1)]
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="antonios.saliba1@gmail.com", password="girgllhuentjkgty")
        connection.sendmail(from_addr="antonios.saliba1@gmail.com", to_addrs="antonios.saliba1@gmail.com", msg=f"Subject:Quote of the day\n\n{random_quote}")