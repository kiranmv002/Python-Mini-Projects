"""
Word Frequency Counter

This program counts how many times each word
appears in a sentence and shows the longest word.

"""

import string

sentence = input("Enter a sentence: ").strip()

if not sentence:
    print("Sentence cannot be empty.")


else:
    # remove punctuation
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))

    words = sentence.lower().split()
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    print("\nWord Frequency:")
    for word in sorted(word_count):
        print(word, ":", word_count[word])

    longest_word = max(words, key=len)
    print("\nLongest word:", longest_word)
