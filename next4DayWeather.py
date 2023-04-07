import requests
import datetime
import os
from dotenv import load_dotenv

url = "https://pro.openweathermap.org/data/2.5/forecast/hourly?"


def get_forecast(api_key, latitude, longitude):
    """
    Get the hourly forecast from OpenWeatherMap
    """
    response = requests.get(
        f'{url}lat={latitude}&lon={longitude}&appid={api_key}')
    return response.json()['list']


def get_header():
    """
    Returns the header for the forecast table.
    """
    return ['Timestamp', 'Temperature', 'Feels Like', 'Min Temperature',
            'Max Temperature', 'Humidity', 'Weather Description']


def get_row_format():
    """
    Returns the row format for the forecast table.
    """
    return '{:<15} {:<20} {:<20} {:<20} {:<20} {:<10} {:<25}'


def get_decorLine():
    """
    Returns the decor line for the forecast table.
    """
    return '-' * 130


def get_title():
    """
    Returns the title for the forecast table.
    """
    return '4-Day Weather Forecast for Ho Chi Minh City'.center(130)


def kelvin_to_celsius(temp):
    """
    Converts temperature from Kelvin to Celsius.
    """
    return temp - 273.15


def get_row(timestamp):
    """
    Returns a row for the forecast table.
    """
    timestamp_str = datetime.datetime.strptime(
        timestamp['dt_txt'], '%Y-%m-%d %H:%M:%S').strftime('%d-%m-%y %H:%M:%S')
    temperature = f"{kelvin_to_celsius(timestamp['main']['temp']):.2f}"
    feels_like = f"{kelvin_to_celsius(timestamp['main']['feels_like']):.2f}"
    min_temp = f"{kelvin_to_celsius(timestamp['main']['temp_min']):.2f}"
    max_temp = f"{kelvin_to_celsius(timestamp['main']['temp_max']):.2f}"
    humidity = timestamp['main']['humidity']
    weather_desc = timestamp['weather'][0]['description']
    if timestamp_str[-8:] == '00:00:00':
        return [f"\n{timestamp_str[:8]}", '', '', '', '', '', '']
    return [timestamp_str[9:-3], temperature, feels_like, min_temp,
            max_temp, humidity, weather_desc]


def write_forecast_to_file(forecast_data, filename):
    """
    Write the forecast data to a file in table format.
    """
    header = get_header()
    row_format = get_row_format()
    decorLine = get_decorLine()
    title = get_title()

    with open(filename, 'w') as file:
        file.write(f"{decorLine}\n{title}\n{decorLine}\n")
        file.write(row_format.format(*header) + '\n')

        for timestamp in forecast_data:
            row = get_row(timestamp)
            row_str = row_format.format(*row)
            file.write(row_str + '\n')


def main():
    load_dotenv()
    api_key = os.getenv("api_key")
    latitude = os.getenv("latitude")
    longitude = os.getenv("longitude")
    forecast_data = get_forecast(api_key, latitude, longitude)
    write_forecast_to_file(forecast_data, 'weather_forecast.txt')


if __name__ == '__main__':
    main()
