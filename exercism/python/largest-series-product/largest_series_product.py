"""Compute the largest product for adjacent digits in a series."""


def largest_product(series: str, size: int) -> int:
    """Return the largest product of `size` adjacent digits from `series`."""
    if size < 0:
        raise ValueError("span must not be negative")

    if size > len(series):
        raise ValueError("span must not exceed string length")

    if not series.isdigit() and series:
        raise ValueError("digits input must only contain digits")

    if not size:
        return 1

    digits = [int(character) for character in series]
    window_product = 0

    for index in range(len(digits) - size + 1):
        product = 1
        for digit in digits[index : index + size]:
            product *= digit
        window_product = max(window_product, product)

    return window_product
