import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv()

base_url = "http://pro.openweathermap.org/data/2.5/"
api_key = os.getenv("api_key")
city = os.getenv("city_name")


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


def get_uv_index(response):
    """
    Gets UV index from API response
    """
    lat = response['coord']['lat']
    lon = response['coord']['lon']
    uv_url = f"{base_url}uvi?appid={api_key}&lat={lat}&lon={lon}"
    uv_response = requests.get(uv_url).json()
    uv_index = uv_response.get('value', None)
    return uv_index


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


def get_weather_data(city):
    """
    Gets weather data from API for specified city
    """
    url = f"{base_url}weather?appid={api_key}&q={city}"
    try:
        response = requests.get(url).json()
        temp_celsius, feels_like_celsius, humidity = get_main_data(
            response)
        description = get_description(response)
        wind_speed = get_wind_data(response)
        sunrise_time, sunset_time = get_sunrise_and_sunset(response)
        uv_index = get_uv_index(response)

        return {
            'city': city,
            'temperature': temp_celsius,
            'feels_like': feels_like_celsius,
            'humidity': humidity,
            'wind_speed': wind_speed,
            'sunrise_time': sunrise_time,
            'sunset_time': sunset_time,
            'description': description,
            'uv_index': uv_index
        }
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def get_city_weather_info(data):
    city = data.get('city', '')
    temperature = data.get('temperature', 0)
    feels_like = data.get('feels_like', 0)
    humidity = data.get('humidity', 0)
    wind_speed = data.get('wind_speed', 0)
    sunrise_time = data.get('sunrise_time', None)
    sunset_time = data.get('sunset_time', None)
    description = data.get('description', '')
    uv_index = data.get('uv_index', None)
    return (city, temperature, feels_like, humidity, wind_speed, sunrise_time, sunset_time, description, uv_index)


def print_weather_header(city_name):
    print(f"{'-'*40}")
    print(f"\tWeather in {city_name}")
    print(f"{'-'*40}")


def print_temperature_info(temperature, feels_like):
    print(f"Temperature:              {temperature:.2f}°C")
    print(f"Feels like:               {feels_like:.2f}°C")


def print_humidity_info(humidity):
    print(f"Humidity:                 {humidity}%")


def print_wind_info(wind_speed):
    print(f"Wind speed:               {wind_speed} km/h")


def print_sunrise_sunset_info(sunrise_time, sunset_time):
    print(f"Sunrise time:             {sunrise_time.strftime('%I:%M %p')}")
    print(f"Sunset time:              {sunset_time.strftime('%I:%M %p')}")


def print_description_info(description):
    print(f"Description:              {description}")


def print_uv_index_info(uv_index):
    if uv_index is not None:
        print(f"UV index:                 {uv_index}")


def print_divider_line():
    print(f"{'-'*40}")


def main():
    data = get_weather_data(city)
    if data is not None:
        city_name, temperature, feels_like, humidity, wind_speed, sunrise_time, sunset_time, description, uv_index = get_city_weather_info(
            data)
        print_weather_header(city_name)
        print_temperature_info(temperature, feels_like)
        print_humidity_info(humidity)
        print_wind_info(wind_speed)
        print_sunrise_sunset_info(sunrise_time, sunset_time)
        print_description_info(description)
        print_uv_index_info(uv_index)
        print_divider_line()


if __name__ == "__main__":
    main()
