# Expense Tracker (CLI)
# This program helps users track daily expenses
# and calculate the total amount spent.

expenses = []


def show_menu():
    print("\nExpense Tracker Menu")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View total amount")
    print("4. Exit")


def add_expense():
    name = input("Enter expense name: ").strip()
    amount = input("Enter amount: ").strip()

    if name == "" or not amount.isdigit():
        print("Invalid expense details.")
        return

    expenses.append({
        "name": name,
        "amount": int(amount)
    })

    print("Expense added successfully.")


def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\nExpenses:")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['name']} - ₹{exp['amount']}")
	print("Total number of expenses:", len(expenses))

def view_total():
    total = sum(exp["amount"] for exp in expenses)
    print(f"Total amount spent: ₹{total}")


def main():
    print("Welcome to Expense Tracker")

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_total()
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
