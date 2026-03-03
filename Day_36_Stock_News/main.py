# ------------------------------------------------- IMPORTS ------------------------------------------------------------- #

import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv
import time

# ------------------------------------------------- CONSTANTS ----------------------------------------------------------- #

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# ------------------------------------------------- GETTING ENV INFO --------------------------------------------------- #

# Write file path to your .env file
dotenv_path = r"C:\Users\anish\OneDrive\Documents\.env"
load_dotenv(dotenv_path=dotenv_path)

# ------------------------------------------------- STOCK DATA -------------------------------------------------------- #

parameters_for_alphavantage = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.getenv("API_KEY_FOR_ALPHA_VINTAGE")
}
url_for_alpha_vantage = "https://www.alphavantage.co/query?"

response_for_alpha_vantage = requests.get(
    url=url_for_alpha_vantage, params=parameters_for_alphavantage)
response_for_alpha_vantage.raise_for_status()
data_for_alpha_vantage = response_for_alpha_vantage.json()[
    "Time Series (Daily)"]
list_of_data = list(data_for_alpha_vantage)

# ------------------------------------------------- CLOSING PRICE ------------------------------------------------------- #

closing_price_list = []
for first_or_second_day in range(2):
    closing_prices = data_for_alpha_vantage[list_of_data[first_or_second_day]]["4. close"]
    closing_price_list.append(float(closing_prices))

# ------------------------------------------------- FUNCTION TO GET NEWS ------------------------------------------------- #


def get_news():
    # ---------- NEWSAPI PARAMETER ---------- #

    parameters_for_newsapi_org = {
        "q": COMPANY_NAME,
        "from": list_of_data[1],
        "sortBy": "publishedAt",
        "language": "en",
        "apiKey": os.getenv("API_KEY_FOR_NEWS_API")
    }

    url_for_news_api_org = "https://newsapi.org/v2/everything?"
    response_for_news_api_org = requests.get(
        url=url_for_news_api_org, params=parameters_for_newsapi_org)
    response_for_news_api_org.raise_for_status()
    data_for_news_api_org = response_for_news_api_org.json()

    if data_for_news_api_org['totalResults'] > 0:
        for each_among_top_3_articles in range(3):
            top_articles = data_for_news_api_org["articles"][each_among_top_3_articles]
            title_for_top_article = top_articles["title"]
            description_for_top_article = top_articles["description"]

            # ---------- Sends sms about article ---------- #

            account_sid_num = os.getenv("SID")
            account_auth_token = os.getenv("AUTH_KEY")
            client = Client(account_sid_num, account_auth_token)

            message = client.messages.create(
                body=f"{COMPANY_NAME}: {percentage_change_in_closing_price}%\nHeadline:{title_for_top_article}\nBrief: {description_for_top_article}",
                from_=os.getenv("TWINUM"),
                to=os.getenv("MYNUM"),
            )

# ------------------------------------------------- CHANGE IN CLOSING PRICE ---------------------------------------------- #

percentage_change_in_closing_price = round((
    (closing_price_list[1]-closing_price_list[0])/closing_price_list[0])*100,2)


# ------------------------------------------------- CHECKS PERCENTAGE CHANGE  --------------------------------------------- #

if -5 >= percentage_change_in_closing_price or percentage_change_in_closing_price >= 5 :
    get_news()
