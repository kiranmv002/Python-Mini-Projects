# CSV Data Analyzer
# Reads a CSV file and shows basic details

import csv

try:
    file = open("data.csv", "r")
    reader = csv.reader(file)

    header = next(reader)
    rows = list(reader)

    file.close()

    print("Columns:", header)
    print("Total rows:", len(rows))

except FileNotFoundError:
    print("CSV file not found.")
