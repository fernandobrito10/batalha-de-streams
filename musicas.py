import requests
from urllib3.exceptions import InsecureRequestWarning
import os
import urllib3
from dotenv import load_dotenv


urllib3.disable_warnings(InsecureRequestWarning)

load_dotenv()

API_KEY = os.getenv("API_KEY")

def get_info_musicas(nome_musica):
    api_url = "https://www.googleapis.com/youtube/v3/search"

    params = {
        "part": "snippet",
        "q": nome_musica,
        "type": "video",
        "maxResults": "1",
        "key": API_KEY
    }

    response = requests.get(api_url, params=params, verify=False)
    data = response.json()
    return {
        "nomeMusica": data["items"][0]["snippet"]["title"],
        "idMusica": data["items"][0]["id"]["videoId"]
    }