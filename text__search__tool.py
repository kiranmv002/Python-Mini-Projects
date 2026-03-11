"""
Text Search Tool

Searches for a word inside a text file.

Author: Kiran
"""

word = input("Enter word to search: ").strip().lower()

if not word:
    print("Search word cannot be empty.")

else:
    try:
        with open("sample.txt", "r") as file:
            content = file.read().lower()

        count = content.count(word)

        if count > 0:
            print(f"'{word}' found {count} times in the file.")
        else:
            print(f"'{word}' not found in the file.")

    except FileNotFoundError:
        print("Text file not found.")
