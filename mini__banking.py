# Mini Banking System
# Simple program to manage balance

balance = 0

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Balance:", balance)

    elif choice == "2":
        amount = int(input("Enter deposit amount: "))
        balance += amount
        print("Amount deposited.")

    elif choice == "3":
        amount = int(input("Enter withdraw amount: "))
        if amount <= balance:
            balance -= amount
            print("Amount withdrawn.")
        else:
            print("Not enough balance.")

    elif choice == "4":
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")
