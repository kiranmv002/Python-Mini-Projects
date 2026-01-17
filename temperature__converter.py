# Temperature Converter (CLI)
# This program converts temperature between
# Celsius and Fahrenheit based on user choice.

def show_menu():
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    print("Welcome to Temperature Converter")

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            value = input("Enter temperature in Celsius: ")
            if not value.replace('.', '', 1).isdigit():
                print("Please enter a valid number.")
                continue

            c = float(value)
            f = celsius_to_fahrenheit(c)
            print(f"{c}°C = {f:.2f}°F")
	    print("Converted from Celsius to Fahrenheit.\n")
	
        elif choice == "2":
            value = input("Enter temperature in Fahrenheit: ")
            if not value.replace('.', '', 1).isdigit():
                print("Please enter a valid number.")
                continue

            f = float(value)
            c = fahrenheit_to_celsius(f)
            print(f"{f}°F = {c:.2f}°C")
	    print("Converted from Fahrenheit to Celsius.\n")
	

        elif choice == "3":
            print("Exiting Temperature Converter. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()




















            
