import requests
from smtplib import *

API_KEY = "b652069ec0d779447589708c55b10138"

parameters = {
    "lat": 33.854721,
    "lon": 35.862286,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
first_3 = data["list"][0]["weather"][0]["id"]
second_3 = data["list"][1]["weather"][0]["id"]
third_3 = data["list"][2]["weather"][0]["id"]
fourth_3 = data["list"][3]["weather"][0]["id"]

print(first_3, second_3, third_3, fourth_3)

if first_3 < 700 or second_3 < 700 or third_3 < 700 or fourth_3 < 700:
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="antonios.saliba1@gmail.com", password="girgllhuentjkgty")
        connection.sendmail(from_addr="antonios.saliba1@gmail.com",
                            to_addrs="antonios.saliba1@gmail.com",
                            msg="Subject: Bring an umbrella\n\nIt will rain in the next 12 hours bring an umbrella with "
                                "you!.")
else:
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="antonios.saliba1@gmail.com", password="girgllhuentjkgty")
        connection.sendmail(from_addr="antonios.saliba1@gmail.com",
                            to_addrs="antonios.saliba1@gmail.com",
                            msg="Subject: Sunny\n\nThe weather is good don't worry.")