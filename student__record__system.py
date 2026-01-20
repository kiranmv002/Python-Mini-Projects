# Student Record Management System
# This program manages student records using a menu-driven approach.

students = []


def show_menu():
    print("\nStudent Record System")
    print("1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Delete student")
    print("5. Exit")


def add_student():
    name = input("Enter student name: ").strip()
    roll_no = input("Enter roll number: ").strip()
    marks = input("Enter marks: ").strip()

    if name == "" or roll_no == "" or not marks.isdigit():
        print("Invalid student details.")
        return

    for student in students:
        if student["roll_no"] == roll_no:
            print("Student with this roll number already exists.")
            return

    students.append({
        "name": name,
        "roll_no": roll_no,
        "marks": int(marks)
    })

    print("Student added successfully.")


def view_students():
    if not students:
        print("No student records available.")
        return

    print("\nStudent Records:")
    for s in students:
        print(f"Name: {s['name']} | Roll No: {s['roll_no']} | Marks: {s['marks']}")


def search_student():
    roll_no = input("Enter roll number to search: ").strip()

    for s in students:
        if s["roll_no"] == roll_no:
            print("\nStudent Found:")
            print(f"Name: {s['name']}")
            print(f"Roll No: {s['roll_no']}")
            print(f"Marks: {s['marks']}")
            return

    print("Student not found.")


def delete_student():
    roll_no = input("Enter roll number to delete: ").strip()

    for s in students:
        if s["roll_no"] == roll_no:
            students.remove(s)
            print("Student record deleted.")
            return

    print("Student not found.")


def main():
    print("Welcome to Student Record Management System")

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting Student Record System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
