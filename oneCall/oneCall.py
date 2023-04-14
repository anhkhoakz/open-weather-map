from printData import *


def main():
    while True:
        print("Please choose an option:")
        print("1. Current Data")
        print("2. Minutely Data")
        print("3. Hourly Data")
        print("4. Daily Data")
        print("5. All Data")
        print("0. Exit")
        try:
            userChoice = int(input("Enter an option: "))
            if userChoice == 1:
                print_current_data()
            elif userChoice == 2:
                print_minutely_data()
            elif userChoice == 3:
                print_hourly_data()
            elif userChoice == 4:
                print_daily_data()
            elif userChoice == 5:
                writeData()
            elif userChoice == 0:
                print("Exiting...")
                break
            else:
                print("Invalid Input!")
        except ValueError:
            print("Invalid Input! Please enter a number.")


if __name__ == "__main__":
    main()
