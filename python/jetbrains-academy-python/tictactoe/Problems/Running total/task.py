number = input()
digits = [int(x) for x in number]
running_total = [sum(digits[:x + 1]) for x in range(0, len(digits))]
print(running_total)
