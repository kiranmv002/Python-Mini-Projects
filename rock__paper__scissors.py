# Rock Paper Scissors Game
# The user plays against the computer.
# The game continues until the user decides to quit.

import random


def play_round(user_choice):
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("Result: It's a tie.")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Result: You win!")
    else:
        print("Result: Computer wins!")


def main():
    print("Rock Paper Scissors")
    print("-------------------")
    print("Type rock, paper, or scissors to play.")
    print("Type quit to exit the game.\n")

    while True:
        user_input = input("Your choice: ").strip().lower()

        if user_input == "quit":
            print("Thanks for playing. See you next time!")
            break

        if user_input not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please try again.\n")
            continue

        play_round(user_input)
        print()  # empty line for better output formatting


if __name__ == "__main__":
    main()
