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


def print_air_quality_info(airLevel):
    if airLevel is not None:
        print(f"Air Quality:              {airLevel}")


def print_divider_line():
    print(f"{'-'*40}")
