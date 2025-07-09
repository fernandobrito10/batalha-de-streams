import requests
from dotenv import load_dotenv
import os
import urllib3
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)

load_dotenv()

API_KEY = os.getenv("API_KEY")

def get_views(video_id):
    api_url = "https://www.googleapis.com/youtube/v3/videos"

    params = {
        "part": "statistics",
        "id": video_id,
        "key": API_KEY
    }
    response = requests.get(api_url, params=params, verify=False)
    if response.status_code != 200:
        print("Erro ao obter token:", response.status_code, response.text)
        return None
    views = response.json()["items"][0]["statistics"]["viewCount"]
    return views
