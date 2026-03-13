"""
Random Quote Generator

This program displays a random quote.
The user can generate quotes multiple times.

Author: Kiran
"""

import random


def show_quote():
    quotes = [
        "Believe in yourself and keep learning.",
        "Practice makes progress, not perfection.",
        "Small steps every day lead to big results.",
        "Consistency is the key to success.",
        "Learning to code is learning to think."
    ]

    quote = random.choice(quotes)
    number = quotes.index(quote) + 1

    print("\nQuote", number)
    print(quote)


def main():
    print("Random Quote Generator")
    print("----------------------")

    while True:
        show_quote()
        again = input("\nDo you want another quote? (y/n): ").lower()

        if again != "y":
            print("Thanks for using the Quote Generator.")
            break


if __name__ == "__main__":
    main()
