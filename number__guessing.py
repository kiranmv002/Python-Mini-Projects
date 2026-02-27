"""
Number Guessing Game

Console-based game where the computer selects
a random number and the user tries to guess it.

Author: Kiran
"""

import random


def choose_difficulty():
    print("\nSelect Difficulty Level:")
    print("1. Easy (1-20)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")

    choice = input("Choose (1/2/3): ")

    if choice == "1":
        return 1, 20, 5
    elif choice == "2":
        return 1, 50, 5
    elif choice == "3":
        return 1, 100, 5
    else:
        print("Invalid choice. Default difficulty selected (1-50).")
        return 1, 50, 5


def play_game():
    start, end, attempts = choose_difficulty()
    secret = random.randint(start, end)

    print("\nI am thinking of a number between", start, "and", end)
    print("You have", attempts, "attempts.\n")

    while attempts > 0:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("Please enter a valid number.\n")
            continue

        guess = int(guess)

        if guess == secret:
            print("Correct! You guessed the number.")
            return
        elif guess < secret:
            print("Too small.\n")
        else:
            print("Too large.\n")

        attempts -= 1
        print("Attempts left:", attempts, "\n")

    print("You lost! The correct number was", secret)


def number_guessing_game():
    print("===== Number Guessing Game =====")

    while True:
        play_game()
        again = input("\nDo you want to play again? (y/n): ").lower()

        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    number_guessing_game()
