import os
from dotenv import load_dotenv

load_dotenv()

base_url = "https://pro.openweathermap.org/"

try:
    load_dotenv()
    api_key = os.getenv("api_key")
    lat = os.getenv("latitude")
    lon = os.getenv("longitude")
except Exception as e:
    print(f"Failed to load environment variables: {e}")
