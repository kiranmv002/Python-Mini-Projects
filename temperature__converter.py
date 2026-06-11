"""
Temperature Converter (CLI)

This program converts temperature between
Celsius, Fahrenheit, and Kelvin.


"""

history = []


def show_menu():
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. View Conversion History")
    print("5. Exit")


def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def celsius_to_kelvin(c):
    return c + 273.15


def main():
    print("Welcome to the Temperature Converter")

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            try:
                c = float(input("Enter temperature in Celsius: "))
                f = celsius_to_fahrenheit(c)
                result = f"{c} °C = {f:.2f} °F"
                print(result)
                history.append(result)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "2":
            try:
                f = float(input("Enter temperature in Fahrenheit: "))
                c = fahrenheit_to_celsius(f)
                result = f"{f} °F = {c:.2f} °C"
                print(result)
                history.append(result)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            try:
                c = float(input("Enter temperature in Celsius: "))
                k = celsius_to_kelvin(c)
                result = f"{c} °C = {k:.2f} K"
                print(result)
                history.append(result)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            if len(history) == 0:
                print("No conversions yet.")
            else:
                print("\nConversion History:")
                for item in history:
                    print(item)

        elif choice == "5":
            print("Exiting Temperature Converter. Goodbye!")
            break


        else:
            print("Invalid choice. Try again.")



if __name__ == "__main__":
    main()
