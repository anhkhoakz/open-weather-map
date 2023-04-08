import requests
import json
import pprint
from config import *


def get_location_data(city_name, country_code):
    limit = 5
    url = f"{base_url}geo/1.0/direct?q={city_name},{country_code}&limit={limit}&appid={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data


def print_location_data(data):
    print("Location data:")
    pprint.pprint(data)


def main():
    city_name = input("Enter your city name:")
    country_code = input("Enter your country code:")
    location_data = get_location_data(city_name, country_code)
    print_location_data(location_data)


if __name__ == "__main__":
    main()
