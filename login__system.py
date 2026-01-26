# Simple Login and Registration System

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        user = input("Username: ")
        pwd = input("Password: ")

        f = open("users.txt", "a")
        f.write(user + "," + pwd + "\n")
        f.close()

        print("Registered successfully.")

    elif choice == "2":
        user = input("Username: ")
        pwd = input("Password: ")
        success = False

        try:
            f = open("users.txt", "r")
            for line in f:
                u, p = line.strip().split(",")
                if u == user and p == pwd:
                    success = True
                    break
            f.close()

            if success:
                print("Login successful.")
            else:
                print("Wrong username or password.")

        except FileNotFoundError:
            print("No users found. Please register first.")

    elif choice == "3":
        print("Exit.")
        break

    else:
        print("Invalid choice.")
