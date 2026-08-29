"""Utilities for finding Pythagorean triplets."""


def triplets_with_sum(number):
    """Return all ordered Pythagorean triplets [a, b, c] where a + b + c == number."""
    triplets = []
    denominator_factor = 2

    # From a^2 + b^2 = c^2 and a + b + c = number we get:
    # b = number * (number - 2a) / (2 * (number - a)).
    # This reduces the search from O(n^2) to O(n).
    for side_a in range(1, (number // 3) + 1):
        numerator = number * (number - (denominator_factor * side_a))
        denominator = denominator_factor * (number - side_a)

        if numerator % denominator:
            continue

        side_b = numerator // denominator
        side_c = number - side_a - side_b

        if side_a < side_b < side_c:
            triplets.append([side_a, side_b, side_c])

    return triplets
