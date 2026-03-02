from twilio.rest import Client
import os
import requests
from dotenv import load_dotenv

# Write your latitude and longtitude
MY_LAT = 0 
MY_LON = 0

# Write path to your .env file 
dotenv_path = r"C:\Users\anish\OneDrive\Documents\.env"  
load_dotenv(dotenv_path=dotenv_path)

# your .env should have 
# "SID" , "AUTH_KEY" , "APPID" , "TWINUM" , "MYNUM"
account_sid_num = os.getenv("SID")
account_auth_token = os.getenv("AUTH_KEY")
client = Client(account_sid_num, account_auth_token)

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": os.getenv("APPID"),
    "cnt": 4,
}

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/forecast?", params=parameters)
response.raise_for_status()
total_weather_data = response.json()

list_of_all_weather = total_weather_data['list']

weather_id = []
number_of_quarters_checked = 0
going_to_rain = False
for _ in list_of_all_weather:
    weather_id_for_each = list_of_all_weather[number_of_quarters_checked]["weather"][0]["id"]
    number_of_quarters_checked += 1
    weather_id.append(weather_id_for_each)
    if weather_id_for_each < 700:
        going_to_rain = True

if going_to_rain:

    message = client.messages.create(
        body="Bring an Umbrella!!",
        from_=os.getenv("TWINUM"),
        to=os.getenv("MYNUM"),
    )
else:
    print("No rain for next 12hrs")
