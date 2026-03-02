import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 0.00  # Your latitude
MY_LONG = 0.00  # Your longitude

# Change these values
MY_GMAIL = "YOUR EMAIL HERE @gmail.com"
MY_PASSWORD = "YOUR APP PASSWORD FOR THE EMAIL ACCOUNT HERE"
SMTP_FOR_GMAIL = "smtp.gmail.com"
YOUR_GMAIL = "THE EMAIL YOU'RE SENDING TO HERE @gmail.com"


def sending_email_to_look_up():
    with smtplib.SMTP(SMTP_FOR_GMAIL) as connection:
        connection.starttls()
        connection.login(user=MY_GMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_GMAIL, to_addrs=YOUR_GMAIL,
                            msg=f"Subject:Look Up!!\n\nThe ISS is right above you.\n Look up!")


while True:
    time.sleep(60)

    response_for_iss = requests.get(
        url="http://api.open-notify.org/iss-now.json")
    response_for_iss.raise_for_status()
    data_for_iss = response_for_iss.json()

    iss_latitude = float(data_for_iss["iss_position"]["latitude"])
    iss_longitude = float(data_for_iss["iss_position"]["longitude"])

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response_for_sun = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response_for_sun.raise_for_status()
    data_for_sun = response_for_sun.json()

    # +5 is added as Nepal's time is UTC + 5
    sunrise = int(data_for_sun["results"]
                  ["sunrise"].split("T")[1].split(":")[0]) + 5
    sunset = int(data_for_sun["results"]
                 ["sunset"].split("T")[1].split(":")[0]) + 5

    current_hour = datetime.now().hour
    diference_in_latitude = iss_latitude - MY_LAT
    diference_in_longitude = iss_longitude - MY_LONG

    if ((-5 <= diference_in_latitude <= 5) and (-5 <= diference_in_longitude <= 5)) and (sunset < current_hour or sunrise > current_hour):
        sending_email_to_look_up()
        print("The iss is visible for you.")

    else:
        print("The iss is not visible for you.")
