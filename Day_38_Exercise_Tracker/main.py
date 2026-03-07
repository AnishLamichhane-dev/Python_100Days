import requests
import datetime as dt
import os
from dotenv import load_dotenv

dotenv_path = r"C:\Users\anish\OneDrive\Documents\.env"
load_dotenv(dotenv_path=dotenv_path)

END_POINT_NUTRIONIX = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
END_POINT_GOOGLE_SHEETS = "https://api.sheety.co/03e0fabb085c8311e7e2953232cfd249/workoutTracking/workouts"

GENDER = "male"
AGE = 16
WEIGHT_KG = 65
HEIGHT_CM = 178

headers = {
    "x-app-id": os.getenv("API_ID_NUTRIONIX"),
    "x-app-key": os.getenv("API_KEY_NUTRIONIX"),
    "Content-Type": "application/json"
}

params = {
    "query": input("Tell me which exercises you did:    "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(END_POINT_NUTRIONIX, json=params, headers=headers)
result = response.json()

for each_exercise in result["exercises"]:

    row_to_add_to_sheets = {
        "workout": {
            "date": dt.datetime.now().strftime("%d/%m/%Y"),
            "time": dt.datetime.now().strftime("%X"),
            "exercise": each_exercise["name"].title(),
            "duration": each_exercise["duration_min"],
            "calories": each_exercise["nf_calories"],
        }

    }
    bearer_headers = {
    "Authorization": f'Bearer "{os.getenv("BEARER_AUTH_GOOGLE_SHEETS")}"'
    }

    sheet_response = requests.post(
        END_POINT_GOOGLE_SHEETS,
        json=row_to_add_to_sheets,
        headers=bearer_headers
    )
    sheet_response.raise_for_status()
