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
    largest_palindrome = None
    factors = []
    for number_a in range(max_factor, min_factor - 1, -1):
        was_bigger = False
        for number_b in range(max_factor, number_a - 1, -1):
            current_product = number_a * number_b
            if largest_palindrome is None or current_product >= largest_palindrome:
                was_bigger = True
                if is_palindrome(current_product):
                    if largest_palindrome is None or current_product > largest_palindrome:
                        factors = []
                        largest_palindrome = current_product
                    factors.append([number_a, number_b])
        if not was_bigger:
            break
    return largest_palindrome, factors


def smallest(max_factor: int, min_factor: int = 0) -> tuple[int | None, list[tuple[int, int]]]:
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param max_factor: int
    :param min_factor: int with a default value of 0
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    validate_inputs(max_factor, min_factor)
    smallest_palindrome = None
    factors = []
    for number_a in range(min_factor, max_factor + 1):
        was_smaller = False
        for number_b in range(number_a, max_factor + 1):
            current_product = number_a * number_b
            if smallest_palindrome is None or current_product <= smallest_palindrome:
                was_smaller = True
                if is_palindrome(current_product):
                    if smallest_palindrome is None or current_product < smallest_palindrome:
                        factors = []
                        smallest_palindrome = current_product
                    factors.append([number_a, number_b])
        if not was_smaller:
            break
    return smallest_palindrome, factors
