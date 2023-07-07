from getData import *
from json import dump


def writeData():
    with open("./oneCall.json", "w") as f:
        dump(data, f, indent=4)
        print("Data written to file successfully.")


def print_current_data():
    sunrise, sunset, temp, feels_like, uvi, description = get_current_data()
    current_data_str = f"Sunrise: {sunrise}, Sunset: {sunset}, Temperature: {temp}, Feels Like: {feels_like}, UV Index: {uvi}, Description: {description}"
    print(current_data_str)


def print_minutely_data():
    precipitation_list = get_minutely_data()
    precipitation_str = ', '.join(str(p) for p in precipitation_list)
    print(f"Precipitation (mm): {precipitation_str}")


def print_hourly_data():
    hourly_data_list = get_hourly_data()
    hourly_data_str = ''
    for hourly_data in hourly_data_list:
        temp, feels_like, uvi, weather = hourly_data
        hourly_data_str += f"Temperature: {temp}, Feels Like: {feels_like}, UV Index: {uvi}, Weather: {weather}\n"
    print(hourly_data_str)


def print_daily_data():
    daily_data_list = get_daily_data()
    daily_data_str = ''
    for daily_data in daily_data_list:
        sunrise, sunset, moonrise, moonset, moon_phase, day_temp, night_temp, max_temp, min_temp, day_feels_like, night_feels_like, uvi, description = daily_data
        daily_data_str += f"Sunrise: {sunrise}, Sunset: {sunset}, Moonrise: {moonrise}, Moonset: {moonset}, Moon Phase: {moon_phase}, Day Temperature: {day_temp}, Night Temperature: {night_temp}, Max Temperature: {max_temp}, Min Temperature: {min_temp}, Day Feels Like: {day_feels_like}, Night Feels Like: {night_feels_like}, UV Index: {uvi}, Description: {description}\n"
    print(daily_data_str)
