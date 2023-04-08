from .getData import get_weather_data, get_city_weather_info
from .printData import *


def main():
    data = get_weather_data()
    if data is not None:
        city_name, temperature, feels_like, humidity, wind_speed, sunrise_time, sunset_time, description, air_quality = get_city_weather_info(
            data)

        print_weather_header(city_name)
        print_temperature_info(temperature, feels_like)
        print_humidity_info(humidity)
        print_wind_info(wind_speed)
        print_sunrise_sunset_info(sunrise_time, sunset_time)
        print_description_info(description)
        print_air_quality_info(air_quality)
        print_divider_line()


if __name__ == "__main__":
    main()
