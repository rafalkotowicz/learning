import sys

word = list(input())
for i in range(len(word) // 2):
    if word[i] != word[-1 - i]:
        print("Not palindrome")
        sys.exit()

print("Palindrome")
