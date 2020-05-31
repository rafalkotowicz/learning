VOWELS = ["a", "e", "i", "o", "u"]
for c in input():
    if c in VOWELS:
        print("vowel")
    elif not c.isalpha():
        break
    else:
        print("consonant")
