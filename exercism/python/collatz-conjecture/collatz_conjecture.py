def steps(number: int) -> int:
    no_of_steps: int = 0

    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    # No need for these lambdas, just practice of syntax
    odd = (lambda x: x / 2)
    even = (lambda x: x * 3 + 1)

    while number != 1:
        if number % 2 == 0:
            number = odd(number)
        else:
            number = even(number)
        no_of_steps += 1

    return no_of_steps
