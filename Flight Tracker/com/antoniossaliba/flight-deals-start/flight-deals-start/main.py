import requests
import datetime as dt
from dateutil.relativedelta import relativedelta
from smtplib import *
import os

API_KEY = os.environ.get("API_KEY")
API_SECRET = os.environ.get("API_SECRET")
OAUTH_TOKEN = os.environ.get("OAUTH_TOKEN")

# parameters = {
#     "grant_type": "client_credentials",
#     "client_id": API_KEY,
#     "client_secret": API_SECRET
# }
#
# headers = {
#     "Content-Type": "application/x-www-form-urlencoded"
# }
#
# response = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token",
#                          data=parameters,
#                          headers=headers)
# response.raise_for_status()
# print(response)
# pprint(response.json())

response1 = requests.get(url="https://api.sheety.co/19d84aeb0e176f1dcf25221e39979bb4/copyOfFlightDeals/prices")
response1.raise_for_status()

sheet_data = response1.json()["prices"]

cities_list = []
lowest_prices = []

for dictionary in sheet_data:

    cities_list.append(dictionary['city'])
    lowest_prices.append(dictionary['lowestPrice'])

iata_codes = []
for city in cities_list:

    parameters = {
        "keyword": city
    }

    headers = {
        "Authorization": OAUTH_TOKEN
    }

    response2 = requests.get(url="https://test.api.amadeus.com/v1/reference-data/locations/cities",
                             params=parameters,
                             headers=headers)

    response2.raise_for_status()
    iata_codes.append(response2.json()["data"][0]["iataCode"])

for i in range(2, len(iata_codes) + 2):

    parameters = {

        "price": {
            "iataCode": iata_codes[i - 2]
        }

    }

    response3 = requests.put(url=f"https://api.sheety.co/19d84aeb0e176f1dcf25221e39979bb4/copyOfFlightDeals/prices/{i}",
                             json=parameters)

idx = 0
for code in iata_codes:

    current_date = str(dt.datetime.now().date())

    parameters = {
        "originLocationCode": "BEY",
        "destinationLocationCode": code,
        "departureDate": current_date,
        "adults": 1
    }

    headers = {
        "Authorization": OAUTH_TOKEN
    }

    response4 = requests.get(url="https://test.api.amadeus.com/v2/shopping/flight-offers",
                             params=parameters,
                             headers=headers)

    the_data_we_need = response4.json()["data"]

    for one_data in the_data_we_need:

        the_price = float(one_data["price"]["total"])

        the_departure_time = one_data["itineraries"][0]["segments"][0]["departure"]["at"]

        the_departure_date = the_departure_time.split("T")[0]

        the_arrival_time = one_data["itineraries"][0]["segments"][0]["arrival"]["at"]

        the_arrival_date = the_arrival_time.split("T")[0]

        the_departure_place = one_data["itineraries"][0]["segments"][0]["departure"]["iataCode"]

        the_arrival_place = one_data["itineraries"][0]["segments"][0]["arrival"]["iataCode"]

        given_date = dt.datetime.strptime(the_departure_date, "%Y-%m-%d")

        now = dt.datetime.now()

        six_months_from_now = now + relativedelta(months=6)

        if given_date <= six_months_from_now and the_price < lowest_prices[idx] and the_arrival_place == code:

            with SMTP("smtp.gmail.com") as connection:

                connection.starttls()
                connection.login(user="antonios.saliba1@gmail.com", password="girgllhuentjkgty")
                connection.sendmail(from_addr="antonios.saliba1@gmail.com",
                                    to_addrs="antonios.saliba1@gmail.com",
                                    msg=f"Subject: Flight Detected!\n\nOnly ${the_price} to fly from "
                                        f"{the_departure_place} "
                                        f"to {the_arrival_place} on "
                                        f"{the_departure_date} "
                                        f"until {the_arrival_date}")

    idx += 1