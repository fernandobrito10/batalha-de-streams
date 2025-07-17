import requests
from dotenv import load_dotenv
import os
import urllib3
from urllib3.exceptions import InsecureRequestWarning
import base64

urllib3.disable_warnings(InsecureRequestWarning)

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = f"{CLIENT_ID}:{CLIENT_SECRET}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    api_url = "https://accounts.spotify.com/api/token"

    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }
    response = requests.post(api_url, headers=headers, data=data, verify=False)
    if response.status_code != 200:
        print("Erro ao obter token:", response.status_code, response.text)
        return None
    print(response.json())
    # token = response.json()["access_token"]
    # return token

get_token()
# token = get_token()
# print(token)