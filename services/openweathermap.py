import requests
import json
from datetime import datetime
from db.mongodb import insert_weather_data
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')
lang = "pt_br"


def get_weather_data(city):
    data = {}
    now = datetime.now()
    geolocation_data = json.loads(
        requests.get(
            f"https://api.openweathermap.org/geo/1.0/direct?q="
            f"{city}&limit=5&appid={API_KEY}&lang={lang}"
        ).text
    )

    for location in geolocation_data:
        lat = location['lat']
        lon = location['lon']
        country = location['country']
        state = location['state']

        source = json.loads(
            requests.get(
                "https://api.openweathermap.org/data/2.5/forecast?"
                "lat={}&lon={}&appid={}&lang={}&units=metric".format(
                    str(lat),
                    str(lon),
                    API_KEY,
                    lang,
                )
            ).text
        )

        for i in source["list"]:
            data[i["dt_txt"]] = [i]


    insert_weather_data(
        json.loads(
            json.dumps(
                data
            )
        )
    )
    
    return data
