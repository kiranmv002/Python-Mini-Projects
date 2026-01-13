"""
Contact Book (Command Line Application)

This program is used to store and manage contact details.
Each contact contains a name and a phone number.
The user can add, view, search, and delete contacts.

Author: Kiran
"""

contacts = []


def menu():
    print("\nContact Book")
    print("1. View all contacts")
    print("2. Add a new contact")
    print("3. Search for a contact")
    print("4. Delete a contact")
    print("5. Exit")


def view_contacts():
    if len(contacts) == 0:
        print("No contacts found.")
        return

    print("\nSaved Contacts:")
    for i in range(len(contacts)):
        print(f"{i + 1}. {contacts[i]['name']} - {contacts[i]['phone']}")


def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()

    if name == "" or phone == "":
        print("Name and phone number cannot be empty.")
        return

    # Check for duplicate contact name
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Contact with this name already exists.")
            return

    contacts.append({
        "name": name,
        "phone": phone
    })

    print("Contact added successfully.")


def search_contact():
    search_name = input("Enter name to search: ").strip().lower()

    for contact in contacts:
        if contact["name"].lower() == search_name:
            print("Contact found:")
            print(contact["name"], "-", contact["phone"])
            return

    print("Contact not found.")


def delete_contact():
    if len(contacts) == 0:
        print("No contacts to delete.")
        return

    view_contacts()
    choice = input("Enter contact number to delete: ")

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    index = int(choice) - 1

    if index < 0 or index >= len(contacts):
        print("Invalid contact number.")
    else:
        removed = contacts.pop(index)
        print(f"Contact '{removed['name']}' deleted.")


def main():
    print("Welcome to the Contact Book Application")

    while True:
        menu()
        option = input("Choose an option (1-5): ")

        if option == "1":
            view_contacts()
        elif option == "2":
            add_contact()
        elif option == "3":
            search_contact()
        elif option == "4":
            delete_contact()
        elif option == "5":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
