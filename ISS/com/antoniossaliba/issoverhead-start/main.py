import requests
import datetime as dt
from smtplib import *

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = round(float(data["iss_position"]["latitude"]))
iss_longitude = round(float(data["iss_position"]["longitude"]))

parameters = {
    "lat": 33.854721,
    "lng": 35.862286,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = dt.datetime.now()
time_now = int(str(time_now).split(" ")[1].split(":")[0])

if (time_now < sunrise or time_now > sunset) and abs(iss_latitude - round(parameters["lat"])) <= 5 and abs(iss_longitude - round(parameters["lng"])) <= 5:
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="antonios.saliba1@gmail.com", password="girgllhuentjkgty")
        connection.sendmail(from_addr="antonios.saliba1@gmail.com",
                            to_addrs="antonios.saliba1@gmail.com",
                            msg="Subject:Look above!\n\nThe ISS is above you!")