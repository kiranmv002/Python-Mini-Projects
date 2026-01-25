# Attendance Management System
# Simple file-based attendance tracker

while True:
    print("\n1. Mark Attendance")
    print("2. View Attendance")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Student name: ").strip()
        status = input("Present or Absent (P/A): ").upper()

        if status in ["P", "A"]:
            file = open("attendance.txt", "a")
            file.write(name + " - " + status + "\n")
            file.close()
            print("Attendance saved.")
        else:
            print("Invalid status.")

    elif choice == "2":
        try:
            file = open("attendance.txt", "r")
            print("\nAttendance Records:")
            print(file.read())
            file.close()
        except FileNotFoundError:
            print("No attendance records found.")

    elif choice == "3":
        print("Exiting Attendance System.")
        break

    else:
        print("Invalid choice.")
