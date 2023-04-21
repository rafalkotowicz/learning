def decimal_to_any_base(decimal: int, output_base: int) -> list[int]:
    number: list[int] = []

    while decimal > 0:
        reminder = decimal % output_base
        number.append(reminder)
        decimal = decimal // output_base

    number.reverse()

    return number if len(number) > 0 else [0]


def rebase(input_base, digits: list[int], output_base) -> list[int]:
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if not all(0 <= digit < input_base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    decimal: int = sum(d * input_base ** i for i, d in enumerate(digits[::-1]))
    result: list[int] = decimal_to_any_base(decimal, output_base)
    return result
