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
    password = ""

    for i in range(length):
        password = password + random.choice(all_characters)

    return password


def start():
    print("Simple Password Generator")
    print("-------------------------")
    print("Generate a strong password in a few seconds.\n")
    user_length = input("Enter password length: ")

    if not user_length.isdigit():
        print("Length must be a number.")
        return

    length = int(user_length)

    if length < 6:
        print("Password length should be at least more 6 characters.")
        return

    if length > 20:
        print("Please choose a password length of 20 characters or less.")
        return

    generated_password = create_password(length)

    print("\nYour generated password is:")
    print(generated_password)
    print("\nNote: Keep this password secure and do not share it with anyone.")
    

if __name__ == "__main__":
    start()
