numbers = []
while True:
    user_input = input()
    if user_input == ".":
        break
    numbers.append(float(user_input))
print(min(numbers))
