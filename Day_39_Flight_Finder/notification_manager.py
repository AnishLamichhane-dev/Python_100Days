from twilio.rest import Client
import os
from dotenv import load_dotenv


class NotificationManager:

    def __init__(self):
        dotenv_path = r"C:\Users\anish\OneDrive\Documents\.env"
        load_dotenv(dotenv_path=dotenv_path)

        account_sid_num = os.getenv("SID")
        account_auth_token = os.getenv("AUTH_KEY")
        self.client = Client(account_sid_num, account_auth_token)

    def send_sms(self, lowest_grand_total, arrival_time_for_cheapest_flight, DATE_FOR_FLIGHT, city_name, city_code):
        """
        Sends sms to user when cheaper deals are found.
        """

        self.message_for_twilio = f"Low price alert! Only ₤{lowest_grand_total} to fly from {os.getenv("ORIGIN_CITY")}-{os.getenv("ORIGIN_CITY_CODE")} to {city_name}-{city_code}, from {DATE_FOR_FLIGHT} to {arrival_time_for_cheapest_flight}."
        message = self.client.messages.create(
            body=f"{self.message_for_twilio}",
            from_=os.getenv("TWINUM"),
            to=os.getenv("MYNUM"),
        )
        print(self.message_for_twilio)
