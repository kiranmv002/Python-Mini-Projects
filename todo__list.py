"""
To-Do List Application (Command Line)

This program allows the user to add, view, and remove tasks
using a simple menu-driven interface. It is created to practice
lists, loops, and user input handling in Python.

Author: Kiran
"""

tasks = []


def show_menu():
    print("\nTo-Do List Menu")
    print("---------------")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print("Task added successfully.")
    else:
        print("Task cannot be empty.")


def remove_task():
    if not tasks:
        print("No tasks to remove.")
        return

    view_tasks()
    choice = input("Enter task number to remove: ")

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    index = int(choice) - 1

    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Task '{removed}' removed.")
    else:
        print("Invalid task number.")


def main():
    print("Simple To-Do List Application")

    while True:
        show_menu()
        option = input("Choose an option (1-4): ")

        if option == "1":
            view_tasks()
        elif option == "2":
            add_task()
        elif option == "3":
            remove_task()
        elif option == "4":
            print("\nYou have exited the To-Do List.")
            print("Good luck with your tasks. See you next time!")
            break
        else:
            print("Invalid option. Please try again.")

	print(f"Total tasks: {len(tasks)}")

if __name__ == "__main__":
    main()
