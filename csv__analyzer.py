# CSV Data Analyzer
# Reads a CSV file and shows basic details

import csv

try:
    file = open("data.csv", "r")
    reader = csv.reader(file)

    header = next(reader)
    rows = list(reader)

    file.close()

    marks = []

    for row in rows:
        marks.append(int(row[2]))  # marks column
    print("Columns:", header)
    print("Total rows:", len(rows))
    print("Highest marks:", max(marks))
    print("Lowest marks :", min(marks))
except FileNotFoundError:
    print("CSV file not found.")
