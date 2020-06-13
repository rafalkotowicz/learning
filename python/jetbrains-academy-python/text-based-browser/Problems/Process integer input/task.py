while True:
    number = int(input())
    if number < 10:
        continue
    elif number > 100:
        break
    else:
        print(number)
