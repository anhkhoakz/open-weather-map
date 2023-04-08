from config import *
import requests


def get_aqi(data):
    try:
        aqi = data["list"][0]["main"]["aqi"]
        return aqi
    except (KeyError, IndexError) as e:
        print("Failed to get AQI:", e)
        return None


def get_air_pollution_level(aqi):
    AQI_LEVELS = {
        1: "Good",
        2: "Fair",
        3: "Moderate",
        4: "Poor",
        5: "Very Poor"
    }
    level = AQI_LEVELS.get(aqi, "Unknown")
    return level


def get_air_pollution_data():
    url = f"{base_url}data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data:
            aqi = get_aqi(data)
            if aqi:
                level = get_air_pollution_level(aqi)
                return level
    except requests.exceptions.RequestException as e:
        print("Failed to fetch data:", e)
        return None
    except ValueError as e:
        print("Failed to parse data:", response.text)
        return None
