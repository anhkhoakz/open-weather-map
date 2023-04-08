from .weather_api import get_forecast
from .weather_report import write_forecast_to_file

def main():
    forecast_data = get_forecast()
    write_forecast_to_file(forecast_data, 'weather_forecast.txt')
    print("The weather forecast for next 4 days has been saved to 'weather_forecast.txt'")

if __name__ == '__main__':
    main()
