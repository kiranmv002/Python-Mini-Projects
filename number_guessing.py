"""
Number Guessing Game

This program was written to practice loops, conditions,
and basic user interaction in Python.

The user has a limited number of attempts to guess
a randomly generated number.

Author: Kiran
"""

import random


def start_game():
    number_to_guess = random.randint(1, 50)
    max_attempts = 5
    attempts = 0

    print("\nNumber Guessing Game")
    print("I have chosen a number between 1 and 50.")
    print("Try to guess it in 5 attempts.\n")

    while attempts < max_attempts:
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        attempts += 1

        if user_guess == number_to_guess:
            print(f"Correct! You guessed the number in {attempts} attempts.")
            break
        elif user_guess < number_to_guess:
            print("Your guess is too low.\n")
        else:
            print("Your guess is too high.\n")

    if user_guess != number_to_guess:
        print(f"Game over. The correct number was {number_to_guess}.")


if __name__ == "__main__":
    start_game()
