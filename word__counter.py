sentence = input("Enter a sentence: ")

words = sentence.lower().split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("\nWord frequency:")
for word in sorted(word_count):
    print(word, ":", word_count[word])

print("\nTotal words:", len(words))
print("Unique words:", len(word_count))

