# Text Search Tool
# Searches for a word inside a text file

word = input("Enter word to search: ").lower()

try:
    file = open("sample.txt", "r")
    content = file.read().lower()
    file.close()

    count = content.count(word)

    if count > 0:
        print(f"'{word}' found {count} times.")
    else:
        print(f"'{word}' not found.")

except FileNotFoundError:
    print("Text file not found.")
