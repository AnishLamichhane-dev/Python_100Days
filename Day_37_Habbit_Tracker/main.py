# ------------------------------------------------- IMPORTS ------------------------------------------------------------- #

import requests
import datetime as dt
import os
from dotenv import load_dotenv

# ------------------------------------------------- CONSTANTS ------------------------------------------------------------- #

USER_NAME = os.getenv("USER_NAME_FOR_PIXELA")
TOKEN = os.getenv("TOKEN_NAME_FOR_PIXELA")
GRAPHID = os.getenv("GRAPH_ID_FOR_PIXELA")
headers = {
    "X-USER-TOKEN": TOKEN
}

# ------------------------------------------------- GETTING ENV INFO --------------------------------------------------- #

# Write file path to your .env file
dotenv_path = r"C:\Users\anish\OneDrive\Documents\.env"
load_dotenv(dotenv_path=dotenv_path)

# ------------------------------------------------- DATE ------------------------------------------------------------- #

today_date = dt.datetime.now()
formatted_date = today_date.strftime("%Y%m%d")

# ------------------------------------------------- ENDPOINTS ------------------------------------------------------------- #

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
post_endpoint = f"{graph_endpoint}/{GRAPHID}"
put_or_delete_endpoint = f"{post_endpoint}/{formatted_date}"

# ------------------------------------------------- PARAMETERS------------------------------------------------------------- #

user_params_pixela = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_config = {
    "id": GRAPHID,
    "name": "Slept",
    "unit": "commit",
    "type": "float",
    "color": "momiji",
    "timezone": "Asia/Kathmandu",
}

post_config = {
    "date": formatted_date,
    "quantity": input("How many hours of sleep did you get??:   "),
}

put_config = {
    "quantity": "8",
}

# ------------------------------------------------- CREATES USER ------------------------------------------------------------- #

# response = requests.post(url=pixela_endpoint, json=user_params_pixela)
# print(response.text, pixela_endpoint)

# ------------------------------------------------- CREATES GRAPH ------------------------------------------------------------- #

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text, graph_endpoint)

# ------------------------------------------------- POSTS COMMITS ------------------------------------------------------------- #

response = requests.put(url=put_or_delete_endpoint,
                        json=put_config, headers=headers)

# ------------------------------------------------- DELETES COMMITS ------------------------------------------------------------- #

# response = requests.delete(url=put_or_delete_endpoint,  headers=headers)
# print(response.text)
