# Mini Banking System
# Simple program to manage balance


balance = 0
transactions = 0
history = []

while True:
    print("\n--- Simple Banking System ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Check Balance
    if choice == "1":
        print(f"\nCurrent Balance: ₹{balance}")
        print(f"Total Transactions: {transactions}")

    # Deposit
    elif choice == "2":
        try:
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                balance += amount
                transactions += 1
                history.append(f"Deposited ₹{amount}")
                print("Amount deposited successfully.")
            else:
                print("Enter a positive amount.")
        except ValueError:
            print("Invalid input! Enter numbers only.")

    # Withdraw
    elif choice == "3":
        try:
            amount = float(input("Enter withdraw amount: "))
            if amount <= 0:
                print("Enter a positive amount.")
            elif amount <= balance:
                balance -= amount
                transactions += 1
                history.append(f"Withdrew ₹{amount}")
                print("Amount withdrawn successfully.")
            else:
                print("Insufficient balance.")
        except ValueError:
            print("Invalid input! Enter numbers only.")

    # Transaction History
    elif choice == "4":
        print("\n--- Transaction History ---")
        if history:
            for item in history:
                print(item)
        else:
            print("No transactions yet.")

    # Exit
    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
