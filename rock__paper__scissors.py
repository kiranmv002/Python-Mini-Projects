"""
Rock Paper Scissors Game

User plays against the computer. Type rock, paper, or scissors to play. Type quit to stop the game.


"""

import random


def play_round(user_choice):
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user_choice == computer:
        print("It's a tie.")
    elif user_choice == "rock" and computer == "scissors":
        print("You win!")
    elif user_choice == "paper" and computer == "rock":
        print("You win!")
    elif user_choice == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("Computer wins!")


def main():
    print("Rock Paper Scissors Game")
    print("------------------------")

    while True:
        user = input("\nEnter rock, paper, scissors or quit: ").lower()

        if user == "quit":
            print("Thanks for playing!")
            break

        if user not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Try again.")
            continue

        play_round(user)


if __name__ == "__main__":
    main()
