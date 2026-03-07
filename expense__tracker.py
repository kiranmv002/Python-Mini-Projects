"""
Expense Tracker (CLI)

This program helps users track daily expenses
and calculate the total amount spent.

Author: Kiran
"""

expenses = []


def show_menu():
    print("\nExpense Tracker Menu")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View total amount")
    print("4. Delete expense")
    print("5. Exit")


def add_expense():
    name = input("Enter expense name: ").strip()

    try:
        amount = float(input("Enter expense amount: "))
    except ValueError:
        print("Invalid amount.")
        return

    expenses.append({
        "name": name,
        "amount": amount
    })

    print("Expense added successfully.")


def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\nExpenses:")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['name']} - ₹{exp['amount']:.2f}")

    total = sum(exp["amount"] for exp in expenses)
    print("Total expenses:", len(expenses))
    print(f"Current total: ₹{total:.2f}")


def view_total():
    total = sum(exp["amount"] for exp in expenses)
    print(f"Total amount spent: ₹{total:.2f}")


def delete_expense():
    if not expenses:
        print("No expenses to delete.")
        return

    view_expenses()
    choice = input("Enter expense number to delete: ")

    if not choice.isdigit():
        print("Invalid number.")
        return

    index = int(choice) - 1

    if 0 <= index < len(expenses):
        removed = expenses.pop(index)
        print(f"Removed expense: {removed['name']}")
    else:
        print("Invalid expense number.")


def main():
    print("Welcome to the Expense Tracker Application")

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_total()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
