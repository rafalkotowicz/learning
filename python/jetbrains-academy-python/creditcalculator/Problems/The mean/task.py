count = 0
sum = 0
average = 0
while True:
    user_input = input().strip()
    if user_input == ".":
        break
    else:
        count += 1
        sum += int(user_input)
        average = sum / count

print(average)
