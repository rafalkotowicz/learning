words = input().split()

frequency_dictionary = {}
for word in words:
    word = word.lower()
    if word not in frequency_dictionary.keys():
        frequency_dictionary[word] = 1
    else:
        frequency_dictionary[word] += 1

for key, value in frequency_dictionary.items():
    print(f"{key} {value}")
