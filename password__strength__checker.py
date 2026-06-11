"""
Password Strength Checker

This program checks the strength of a password
based on multiple security rules.


"""


def check_password_strength(password):
    length_ok = len(password) >= 8
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_special = any(not char.isalnum() for char in password)

    score = sum([length_ok, has_digit, has_upper, has_lower, has_special])

    if score == 5:
        return "Strong 💪"
    elif score >= 3:
        return "Medium 👍"
    else:
        return "Weak ❌"


def main():
    print("===== Password Strength Checker =====")
    password = input("Enter a Password: ")

    strength = check_password_strength(password)
    print(f"Password Strength: {strength}")


if __name__ == "__main__":
    main()
