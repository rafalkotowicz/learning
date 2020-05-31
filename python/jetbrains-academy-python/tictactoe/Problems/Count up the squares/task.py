total = 0
numbers = []
while True:
    number = int(input().strip())
    numbers.append(number)
    total += number
    if total == 0:
        print(sum([x ** 2 for x in numbers]))
        break
