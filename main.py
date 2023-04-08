from currentWeather.main import main as getCurrent
from next4DayWeather.main import main as getFourDay
from getDirectGeocoding.main import main as DirectGeocoding


def main():
    while True:
        print("Please choose an option:")
        print("1. Get current weather")
        print("2. Get next 4 days weather")
        print("3. Get direct geocoding")
        print("4. Exit")
        try:
            userChoice = int(input("Enter an option: "))
            if userChoice == 1:
                getCurrent()
            elif userChoice == 2:
                getFourDay()
            elif userChoice == 3:
                DirectGeocoding()
            elif userChoice == 4:
                print("Exiting...")
                break
            else:
                print("Invalid Input!")
        except ValueError:
            print("Invalid Input! Please enter a number.")


if __name__ == "__main__":
    main()
