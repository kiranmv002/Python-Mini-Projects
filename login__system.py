"""
Simple Login and Registration System

This program allows users to register and login
using a text file.

"""

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        user = input("Username: ").strip()
        pwd = input("Password: ").strip()

        if not user or not pwd:
            print("Username and password cannot be empty.")
            continue

        # check duplicate username
        exists = False
        try:
            with open("users.txt", "r") as f:
                for line in f:
                    u, _ = line.strip().split(",")
                    if u == user:
                        exists = True
                        break
        except FileNotFoundError:
            pass

        if exists:
            print("Username already exists. Try another.")
        else:
            with open("users.txt", "a") as f:
                f.write(user + "," + pwd + "\n")
            print("Registered successfully.")

    elif choice == "2":
        user = input("Username: ").strip()
        pwd = input("Password: ").strip()

        success = False

        try:
            with open("users.txt", "r") as f:
                for line in f:
                    u, p = line.strip().split(",")
                    if u == user and p == pwd:
                        success = True
                        break

            if success:
                print("Login successful.")
            else:
                print("Wrong username or password.")

        except FileNotFoundError:
            print("No users found. Please register first.")

    elif choice == "3":
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")
