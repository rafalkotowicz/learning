def factors(value):
    result: [int] = []

    divisor = 2
    current_val: int = value
    while current_val > 1:
        if current_val % divisor == 0:
            result.append(divisor)
            current_val /= divisor
        else:
            divisor += 1

    return result
