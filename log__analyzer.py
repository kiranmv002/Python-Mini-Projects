# Simple Log File Analyzer
# Counts different types of log messages

errors = 0
warnings = 0
infos = 0

try:
    file = open("sample.log", "r")

    for line in file:
        if "ERROR" in line:
            errors += 1
        elif "WARNING" in line:
            warnings += 1
        elif "INFO" in line:
            infos += 1

    file.close()

    print("\nLog Report")
    print("Errors  :", errors)
    print("Warnings:", warnings)
    print("Info    :", infos)

except FileNotFoundError:
    print("Log file not found.")
