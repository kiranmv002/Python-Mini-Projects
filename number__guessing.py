"""
Number Guessing Game

This is a small console-based game written in Python.
The computer chooses a random number and the user
tries to guess it with the help of hints.

Author: Kiran
"""

import random


def play_game():
    start = 1
    end = 50
    secret = random.randint(start, end)
    attempts = 5

    print("\nI am thinking of a number between", start, "and", end)
    print("You have", attempts, "chances to guess it correctly.\n")

    while attempts > 0:
        user_input = input("Enter your guess: ")

        if not user_input.isdigit():
            print("Please enter a valid number.\n")
            continue

        guess = int(user_input)

        if guess == secret:
            print("Well done! You guessed the correct number.")
            return
        elif guess < secret:
            print("Your guess is too small.\n")
        else:
            print("Your guess is too large.\n")

        attempts -= 1
        print("Attempts remaining:", attempts, "\n")

    print("You have used all attempts. The number was", secret)


def number_guessing_game():
    print("Number Guessing Game")
    print("-------------------")

    while True:
        play_game()
        again = input("\nDo you want to play again? (y/n): ").lower()

        if again != "y":
           print("Game over! Thanks for playing the number guessing game.")
           break


if __name__ == "__main__":
    number_guessing_game()

