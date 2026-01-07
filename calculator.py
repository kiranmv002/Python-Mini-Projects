"""Simple Calculator (CLI Based)

This program is created to practice basic Python concepts
like functions, conditions, and user input handling.

Author: Kiran
"""

def show_menu():
    print("\n====== CALCULATOR MENU ======")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Multiply two numbers")
    print("4. Divide two numbers")
    print("5. Modulus")
    print("6. Exit")


def add_numbers(x, y):
    return x + y

def subtract_numbers(x, y):
    return x - y


def multiply_numbers(x, y):
    return x * y


def divide(a, b):
    """Returns the division of two numbers"""
    if b == 0:
        return "Error: Division by zero"
    return a / b

def modulus_numbers(x, y):
    return x % y

def main():
    print("Welcome to Simple Calculator")

    while True:
        show_menu()
        choice = input("Enter your choice (1–5): ")

        if choice == "5":
            print("Thank you for using the calculator.")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice! Please select again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numeric values.")
            continue

        if choice == "1":
            result = add_numbers(num1, num2)
            operation = "Addition"
        elif choice == "2":
            result = subtract_numbers(num1, num2)
            operation = "Subtraction"
        elif choice == "3":
            result = multiply_numbers(num1, num2)
            operation = "Multiplication"
        elif choice == "4":
            result = divide_numbers(num1, num2)
            operation = "Division"

        print(f"{operation} Result: {result}")


if __name__ == "__main__":
    main()
