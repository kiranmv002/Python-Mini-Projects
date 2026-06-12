"""
CSV Data Analyzer

Reads a CSV file and shows basic details.


"""

import csv

try:
    with open("data.csv", "r") as file:
        reader = csv.reader(file)

        header = next(reader)
        rows = list(reader)

    marks = []

    for row in rows:
        try:
            marks.append(int(row[2]))  # marks column
        except:
            continue  # skip invalid rows

    print("Columns:", header)
    print("Total rows:", len(rows))

    if marks:
        print("Highest marks:", max(marks))
        print("Lowest marks :", min(marks))
        avg = sum(marks) / len(marks)
        print("Average marks:", round(avg, 2))
    else:
        print("No valid marks found.")

except FileNotFoundError:
    print("CSV file not found.")
