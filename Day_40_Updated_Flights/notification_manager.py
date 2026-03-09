from twilio.rest import Client
import smtplib
import os
from dotenv import load_dotenv


class NotificationManager:

    def __init__(self):
        dotenv_path = r"C:\Users\anish\OneDrive\Documents\.env"
        load_dotenv(dotenv_path=dotenv_path)

        account_sid_num = os.getenv("SID")
        account_auth_token = os.getenv("AUTH_KEY")
        self.client = Client(account_sid_num, account_auth_token)

    def send_sms(self, lowest_grand_total, arrival_time_for_cheapest_flight, DATE_FOR_FLIGHT, city_name, city_code, list_of_total_stop_overs):
        """
        Sends sms to user when cheaper deals are found.
        """

        self.message_to_send = f"Only {lowest_grand_total} pounds to fly from {os.getenv("ORIGIN_CITY")}-{os.getenv("ORIGIN_CITY_CODE")} to {city_name}-{city_code}, from {DATE_FOR_FLIGHT} to {arrival_time_for_cheapest_flight}.\n\nFlight has {len(list_of_total_stop_overs)} stop overs, via IATA Codes {'-'.join(str(each_stop_over) for each_stop_over in list_of_total_stop_overs)}".encode('utf-8')
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login("minecrafteranish@gmail.com",
                         os.getenv("MY_GMAIL_APP_PASSWORD"))
        connection.sendmail(from_addr=os.getenv("MY_GMAIL_FOR_SMTP"),
                            to_addrs=os.getenv("THE_GMAIL_TO_SEND_EMAIL"),
                            msg=f"Subject: Low price alert!!\n\n {self.message_to_send}.")

        message = self.client.messages.create(
            body=f"Low price alert! {self.message_to_send}",
            from_=os.getenv("TWINUM"),
            to=os.getenv("MYNUM"),
        )

        print(self.message_to_send)

    def send_emails(self, all_emails):
        """
        Sends email to all the users who have registered.
        """

        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login("minecrafteranish@gmail.com",
                         os.getenv("MY_GMAIL_APP_PASSWORD"))
        for each_email in all_emails:
            try:
                connection.sendmail(from_addr="minecrafteranish@gmail.com",
                                    to_addrs=each_email,
                                    msg=f"Subject: Low price alert!!\n\n {self.message_to_send}.")
            except:
                continue
            else:
                connection.sendmail(from_addr="minecrafteranish@gmail.com",
                                    to_addrs=each_email,
                                    msg=f"Subject: Low price alert!!\n\n {self.message_to_send}.")
