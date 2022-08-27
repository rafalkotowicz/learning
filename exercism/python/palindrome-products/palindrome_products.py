# UNFINISHED: needs performance improvement (works, but is too slow)

def validate_inputs(max_factor: int, min_factor: int = 0) -> None:
    if min_factor > max_factor:
        raise ValueError("min must be <= max")


def is_palindrome(number: int) -> bool:
    str_number = str(number)
    return str_number == str_number[::-1]


def largest(max_factor: int, min_factor: int = 0):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param max_factor: int
    :param min_factor: int with a default value of 0
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    validate_inputs(max_factor, min_factor)

    factors: list((int, int)) = []
    products = []
    for num_a in range(min_factor, max_factor + 1):
        for num_b in range(min_factor, max_factor + 1):
            products.append(num_a * num_b)

    products.sort(reverse=True)

    for product in products:
        if is_palindrome(product):
            for num_c in range(min_factor, max_factor + 1):
                for num_d in range(min_factor, max_factor + 1):
                    if num_c * num_d == product:
                        factors.append((num_c, num_d))
            return product, factors
    return None, factors


def smallest(max_factor: int, min_factor: int = 0):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param max_factor: int
    :param min_factor: int with a default value of 0
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    validate_inputs(max_factor, min_factor)

    factors: list((int, int)) = []
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
