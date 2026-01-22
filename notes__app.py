# Simple Notes Application
# This program saves notes in a text file.

choice = ""

while choice != "3":
    print("\nNotes App")
    print("1. Add note")
    print("2. View notes")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        note = input("Enter note: ").strip()
	if not note:
    	   print("Note cannot be empty.")
           continue

	if note:
            file = open("notes.txt", "a")
            file.write(note + "\n")
            file.close()
            print("Note saved.")

    elif choice == "2":
        try:
            file = open("notes.txt", "r")
            print("\nYour Notes:")
            print(file.read())
            file.close()
        except FileNotFoundError:
            print("No notes found.")

    elif choice == "3":
        print("Exiting Notes App.")

    else:
        print("Invalid choice.")
