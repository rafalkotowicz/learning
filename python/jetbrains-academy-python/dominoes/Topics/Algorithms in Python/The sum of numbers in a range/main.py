def range_sum(numbers, start, end):
    total = 0
    for number in numbers:
        if start <= number <= end:
            total += number
    return total


input_numbers = input().split()
a, b = input().split()
print(range_sum([int(i) for i in input_numbers], int(a), int(b)))
