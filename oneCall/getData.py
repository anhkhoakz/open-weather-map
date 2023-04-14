from utils import *
import requests
from config import lat, lon, api_key


ONECALL_BASE_URL = "https://pro.openweathermap.org/data/2.5/onecall"
url = f"{ONECALL_BASE_URL}?lat={lat}&lon={lon}&appid={api_key}"
response = requests.get(url)
data = response.json()


def get_current_data():
    current_data = data['current']

    sunrise = unix_to_normal_time(current_data['sunrise'])
    sunset = unix_to_normal_time(current_data['sunset'])
    temp = kelvin_to_celsius(current_data['temp'])
    feels_like = kelvin_to_celsius(current_data['feels_like'])
    uvi = current_data['uvi']
    description = current_data['weather'][0]['description']

    return sunrise, sunset, temp, feels_like, uvi, description


def get_minutely_data():
    minutely_data = data['minutely']
    precipitation_list = [minutely_data[i]['precipitation'] for i in range(61)]
    return precipitation_list


def get_hourly_data():
    hourly_data = data['hourly']
    hourly_data_list = []
    for i in range(48):
        temp = kelvin_to_celsius(hourly_data[i]['temp'])
        feels_like = kelvin_to_celsius(hourly_data[i]['feels_like'])
        uvi = hourly_data[i]['uvi']
        pop = hourly_data[i]['pop']
        weather = hourly_data[i]['weather'][0]['description']
        hourly_data_list.append((temp, feels_like, uvi, weather))
    return hourly_data_list


def get_daily_data():
    daily_data = data['daily']
    daily_data_list = []
    for i in range(8):
        sunrise = unix_to_normal_time(daily_data[i]['sunrise'])
        sunset = unix_to_normal_time(daily_data[i]['sunset'])
        moonrise = unix_to_normal_time(daily_data[i]['moonrise'])
        moonset = unix_to_normal_time(daily_data[i]['moonset'])
        moon_phase = get_moon_phase(daily_data[i]['moon_phase'])
        daily_data_temp = daily_data[i]['temp']
        day_temp = kelvin_to_celsius(daily_data_temp['day'])
        night_temp = kelvin_to_celsius(daily_data_temp['night'])
        max_temp = kelvin_to_celsius(daily_data_temp['max'])
        min_temp = kelvin_to_celsius(daily_data_temp['min'])
        daily_data_feels_like = daily_data[i]['feels_like']
        day_feels_like = kelvin_to_celsius(daily_data_feels_like['day'])
        night_feels_like = kelvin_to_celsius(daily_data_feels_like['night'])
        uvi = daily_data[i]['uvi']
        pop = daily_data[i]['pop']
        description = daily_data[i]['weather'][0]['description']
        daily_data_list.append((sunrise, sunset, moonrise, moonset, moon_phase, day_temp,
                               night_temp, max_temp, min_temp, day_feels_like, night_feels_like, uvi, description))
    return daily_data_list
