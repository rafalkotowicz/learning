# UNFINISHED: needs performance improvement (works, but is too slow)

def validate_inputs(max_factor: int, min_factor: int = 0) -> None:
    if min_factor > max_factor:
        raise ValueError("min must be <= max")


def is_palindrome(number: int) -> bool:
    str_number = str(number)
    return str_number == str_number[::-1]


def largest(max_factor: int, min_factor: int = 0) -> tuple[int | None, list[tuple[int, int]]]:
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param max_factor: int
    :param min_factor: int with a default value of 0
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    validate_inputs(max_factor, min_factor)

    results = dict()
    palindromes = []
    for num_a in range(min_factor, max_factor + 1):
        for num_b in range(min_factor, max_factor + 1):
            product = num_a * num_b
            if is_palindrome(product):
                if results.get(product):
                    results[product].append((num_a, num_b))
                else:
                    results[product] = [(num_a, num_b)]
                palindromes.append(product)

    largest_palindrome = max(palindromes) if palindromes else None
    if largest_palindrome:
        return largest_palindrome, results[largest_palindrome]
    else:
        return None, []

    
    # results = dict()
    # palindromes = []
    # pairs = set()
    # for num_a in range(min_factor, max_factor + 1):
    #     for num_b in range(min_factor, max_factor + 1):
    #         if num_a < num_b:
    #             pairs.add((num_a, num_b))
    #         else:
    #             pairs.add((num_b, num_a))

    # for pair in pairs:
    #     product = pair[0] * pair[1]
    #     if is_palindrome(product):
    #         if results.get(product):
    #             results[product].append(pair)
    #         else:
    #             results[product] = [pair]
    #         palindromes.append(product)

    # largest_palindrome = max(palindromes) if palindromes else None
    # if largest_palindrome:
    #     return largest_palindrome, results[largest_palindrome]
    # else:
    #     return None, []

def smallest(max_factor: int, min_factor: int = 0) -> tuple[int | None, list[tuple[int, int]]]:
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param max_factor: int
    :param min_factor: int with a default value of 0
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    validate_inputs(max_factor, min_factor)

    factors: list[tuple[int, int]] = []
    for num_a in range(min_factor, max_factor + 1):
        for num_b in range(min_factor, max_factor + 1):
            product = num_a * num_b
            if is_palindrome(product):
                for num_c in range(min_factor, max_factor + 1):
                    for num_d in range(min_factor, max_factor + 1):
                        if num_c * num_d == product:
                            factors.append((num_c, num_d))
                return product, factors
    return None, factors
