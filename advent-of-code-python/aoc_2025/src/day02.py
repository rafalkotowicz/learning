def puzzle_1(input: str):
    ranges = input.split(',')

    sum = 0
    for _range in ranges:
        start, end = [int(x) for x in _range.split('-')]

        for x in range(start, end + 1):
            as_string = str(x)
            left = as_string[len(as_string)//2:]
            right = as_string[:len(as_string)//2]

            if left == right:
                sum += x

    return sum

