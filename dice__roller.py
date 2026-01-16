# Dice Rolling Simulator
# This program simulates rolling a dice using Python.
# The user can roll the dice multiple times if they want.

import random


def roll_dice():
    return random.randint(1, 6)


def main():
    print("Dice Rolling Simulator")
    print("----------------------")
    roll_count = 0
    while True:
        choice = input("Roll the dice? (y/n): ").strip().lower()

        if choice == "y":
            result = roll_dice()
            roll_count += 1
            print(f"You rolled a {result}")
            print(f"Total rolls so far: {roll_count}\n")

        elif choice == "n":
            print("Thanks for playing. Goodbye!")
            break
        else:
            print("Please enter y or n.\n")


if __name__ == "__main__":
    main()
