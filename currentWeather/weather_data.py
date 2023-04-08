import datetime
import requests
from config import *


def kelvin_to_celsius(kelvin):
    """
    Converts temperature in Kelvin to Celsius
    """
    return kelvin - 273.15


def get_description(response):
    """
    Gets weather description from API response
    """
    weather = response.get('weather', [{}])[0]
    return weather.get('description', '')


def get_wind_data(response):
    """
    Gets wind speed from API response
    """
    wind = response.get('wind', {})
    return wind.get('speed', 0)


def get_sunrise_and_sunset(response):
    """
    Gets sunrise and sunset times from API response
    """
    sys = response.get('sys', {})
    timezone = response.get('timezone', 0)
    sunrise_time = datetime.datetime.utcfromtimestamp(
        sys.get('sunrise', 0) + timezone)
    sunset_time = datetime.datetime.utcfromtimestamp(
        sys.get('sunset', 0) + timezone)
    return sunrise_time, sunset_time


def get_main_data(response):
    """
    Gets main weather data from API response
    """
    main = response.get('main', {})
    temp_kelvin = main.get('temp', 0)
    temp_celsius = kelvin_to_celsius(temp_kelvin)
    feels_like_kelvin = main.get('feels_like', 0)
    feels_like_celsius = kelvin_to_celsius(feels_like_kelvin)
    humidity = main.get('humidity', 0)
    return temp_celsius, feels_like_celsius, humidity


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


def get_weather_data():
    """
    Gets weather data from API for specified city
    """

    url = f"{base_url}data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    try:
        response = requests.get(url).json()
        temp_celsius, feels_like_celsius, humidity = get_main_data(
            response)
        description = get_description(response)
        wind_speed = get_wind_data(response)
        sunrise_time, sunset_time = get_sunrise_and_sunset(response)

        return {
            'city': get_location(),
            'temperature': temp_celsius,
            'feels_like': feels_like_celsius,
            'humidity': humidity,
            'wind_speed': wind_speed,
            'sunrise_time': sunrise_time,
            'sunset_time': sunset_time,
            'description': description,
        }
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
