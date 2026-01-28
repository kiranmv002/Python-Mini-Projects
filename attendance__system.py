# Attendance Management System
# Improved version with summary count


present = 0
absent = 0

while True:
    print("\n1. Mark Attendance")
    print("2. View Attendance")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Student name: ").strip()
        status = input("Present or Absent (P/A): ").upper()

        if status == "P":
            present += 1
        elif status == "A":
            absent += 1
        else:
            print("Invalid status.")
            continue

        file = open("attendance.txt", "a")
        file.write(name + " - " + status + "\n")
        file.close()
        print("Attendance saved.")

    elif choice == "2":
        try:
            file = open("attendance.txt", "r")
            print("\nAttendance Records:")
            print(file.read())
            file.close()

            print("Total Present:", present)
            print("Total Absent :", absent)

        except FileNotFoundError:
            print("No attendance records found.")

    elif choice == "3":
        print("Exiting Attendance System.")
        break

    else:
        print("Invalid choice.")

