sentence = input("Enter a sentence: ")

words = sentence.lower().split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("\nWord frequency:")
for word in sorted(word_count):
    print(word, ":", word_count[word])

longest_word = max(word_count, key=len)
print("Longest word:", longest_word)

