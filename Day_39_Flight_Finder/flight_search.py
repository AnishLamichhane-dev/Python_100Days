import amadeus
import os
from dotenv import load_dotenv
import datetime as dt



class FlightSearch:

    def __init__(self, each_city_iata_code):
        dotenv_path = r"C:\Users\anish\OneDrive\Documents\.env"
        load_dotenv(dotenv_path=dotenv_path)

        self.DATE_FOR_FLIGHT = dt.datetime.now().strftime("%Y-%m-%d")  # "YYYY-MM-DD"

        self.amadeus = amadeus.Client(
            client_id=os.getenv("KEY_FOR_AMADEUS"),
            client_secret=os.getenv("SECRET_FOR_AMADEUS")
        )

        self.response_amadeus = self.amadeus.shopping.flight_offers_search.get(
            originLocationCode=os.getenv("ORIGIN_CITY_CODE"),
            destinationLocationCode=each_city_iata_code,
            departureDate=self.DATE_FOR_FLIGHT,
            adults='1'
        )
