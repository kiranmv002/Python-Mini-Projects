"""
Attendance Management System (Improved Version)

Features:
- Mark student attendance
- View attendance records
- Automatically calculates total Present and Absent
- Uses proper file handling (with open)

Author: Kiran
"""


def count_attendance():
    """Counts total Present and Absent from file"""
    present = 0
    absent = 0

    try:
        with open("attendance.txt", "r") as file:
            for line in file:
                if "- P" in line:
                    present += 1
                elif "- A" in line:
                    absent += 1
    except FileNotFoundError:
        pass

    return present, absent


def mark_attendance():
    """Marks attendance for a student"""
    name = input("Student name: ").strip()
    status = input("Present or Absent (P/A): ").upper()

    if status not in ["P", "A"]:
        print("Invalid status. Please enter P or A.")
        return

    with open("attendance.txt", "a") as file:
        file.write(name + " - " + status + "\n")

    print("Attendance saved successfully.")


def view_attendance():
    """Displays attendance records and summary"""
    try:
        with open("attendance.txt", "r") as file:
            print("\nAttendance Records:")
            print(file.read())

        present, absent = count_attendance()
        total = present + absent

        print("Total Students:", total)
        print("Total Present :", present)
        print("Total Absent  :", absent)

        if total > 0:
            percentage = (present / total) * 100
            print("Attendance Percentage: {:.2f}%".format(percentage))

    except FileNotFoundError:
        print("No attendance records found.")


def main():
    print("===== Attendance Management System =====")

    while True:
        print("\n1. Mark Attendance")
        print("2. View Attendance")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            mark_attendance()

        elif choice == "2":
            view_attendance()

        elif choice == "3":
            print("Exiting Attendance System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select again.")


if __name__ == "__main__":
    main()
