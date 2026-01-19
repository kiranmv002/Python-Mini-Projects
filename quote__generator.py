# Random Quote Generator
# This program displays a random quote each time it runs.

import random


def show_quote():
    quotes = [
        "Believe in yourself and keep learning.",
        "Practice makes progress, not perfection.",
        "Small steps every day lead to big results.",
        "Consistency is the key to success.",
        "Learning to code is learning to think."
    ]

    selected_quote = random.choice(quotes)
    print("\nQuote of the Day:")
    print(selected_quote)


def main():
    print("Random Quote Generator")
    print("----------------------")
    show_quote()


if __name__ == "__main__":
    main()
