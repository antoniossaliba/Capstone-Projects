import requests
import datetime as dt
from smtplib import *
from email.mime.text import MIMEText

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "AN4N93QHEHVEE9LK"
NEWS_API_KEY = "c548bcd5ffd243399f83eb594053de9d"

data_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY
}

response1 = requests.get(url="https://www.alphavantage.co/query", params=data_parameters)
response1.raise_for_status()
data = response1.json()

yesterday = str((dt.datetime.now() - dt.timedelta(days=1)).date())
before_yesterday = str((dt.datetime.now() - dt.timedelta(days=2)).date())

yesterday_closure_stock_price = float(data["Time Series (Daily)"][yesterday]["4. close"])
before_yesterday_closure_stock_price = float(data["Time Series (Daily)"][before_yesterday]["4. close"])

difference = abs(yesterday_closure_stock_price - before_yesterday_closure_stock_price)

diff_percentage = difference / yesterday_closure_stock_price * 100

if diff_percentage > 3:

    news_parameters = {
        "q": COMPANY_NAME,
        "from": yesterday,
        "sortBy": "publishedAt",
        "apikey": NEWS_API_KEY
    }

    response2 = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    response2.raise_for_status()
    news_data = response2.json()

    with SMTP("smtp.gmail.com") as connection:
        msg = MIMEText(f"{news_data['articles'][0]['description']}", _charset="utf-8")
        msg["Subject"] = f"{news_data['articles'][0]['title']}"
        connection.starttls()
        connection.login(user="antonios.saliba1@gmail.com", password="girgllhuentjkgty")
        connection.sendmail(from_addr="antonios.saliba1@gmail.com",
                            to_addrs="antonios.saliba1@gmail.com",
                            msg=msg.as_string())