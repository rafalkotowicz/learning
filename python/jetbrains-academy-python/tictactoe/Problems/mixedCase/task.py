sample = input()
words = sample.split()
capitalized_words = [words[0]]
capitalized_words.extend([word.capitalize() for word in words if word is not words[0]])
print("".join(capitalized_words))
