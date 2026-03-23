"""
Password Generator (Console Based)

This program creates a random password using
letters, numbers, and special symbols.

It was written to practice loops, conditions,
and basic user input handling.

Author: Kiran
"""

import random

print("Tip: Use strong passwords and avoid reusing them.")


def create_password(length):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+-="

    all_characters = letters + numbers + symbols

    # generate password
    password = "".join(random.choice(all_characters) for _ in range(length))

    return password


def start():
    print("\nSimple Password Generator")
    print("-------------------------")

    user_length = input("Enter password length: ")

    if not user_length.isdigit():
        print("Length must be a number.")
        return

    length = int(user_length)

    if length < 6:
        print("Password must be at least 6 characters.")
        return

    if length > 20:
        print("Maximum length allowed is 20.")
        return

    password = create_password(length)

    print("\nGenerated Password:")
    print(password)
    print("Password length:", len(password))

    print("\nNote: Keep this password secure.")


if __name__ == "__main__":
    start()

if __name__ == "__main__":
    start()
