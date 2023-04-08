from .air_quality_data import *
from .weather_data import *


def get_city_weather_info(data):
    city = data.get('city', '')
    temperature = data.get('temperature', 0)
    feels_like = data.get('feels_like', 0)
    humidity = data.get('humidity', 0)
    wind_speed = data.get('wind_speed', 0)
    sunrise_time = data.get('sunrise_time', None)
    sunset_time = data.get('sunset_time', None)
    description = data.get('description', '')
    air_quality = get_air_pollution_data()

    return (city, temperature, feels_like, humidity, wind_speed, sunrise_time, sunset_time, description, air_quality)
