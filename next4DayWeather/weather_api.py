import requests
from config import *


def get_location():
    """
    Gets location data from API for specified coordinate
    """
    limit = 1
    url = f"{base_url}geo/1.0/reverse?lat={lat}&lon={lon}&limit={limit}&appid={api_key}"
    try:
        response = requests.get(url).json()
        name_value = response[0]['name']
        return name_value
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def get_forecast():
    """
    Get the hourly forecast from OpenWeatherMap
    """
    response = requests.get(
        f'{base_url}data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={api_key}')
    return response.json()['list']
