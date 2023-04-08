import os
import datetime
from .weather_api import get_location


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
    return f'4-Day Weather Forecast for {get_location()}'.center(130)


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

    # construct the parent directory path using ".."
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    file_path = os.path.join(parent_dir, filename)
    with open(file_path, 'w') as file:
        file.write(f"{decorLine}\n{title}\n{decorLine}\n")
        file.write(row_format.format(*header) + '\n')

        for timestamp in forecast_data:
            row = get_row(timestamp)
            row_str = row_format.format(*row)
            file.write(row_str + '\n')
