# Password Strength Checker
# This program checks the strength of a password
# based on simple rules.

password = input("Enter a password: ")

length_ok = len(password) >= 8
has_digit = any(char.isdigit() for char in password)
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)

if length_ok and has_digit and has_upper and has_lower:
    print("Password Strength: Strong")
elif length_ok and has_digit:
    print("Password Strength: Medium")
else:
    print("Password Strength: Weak")
