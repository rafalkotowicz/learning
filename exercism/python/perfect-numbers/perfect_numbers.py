def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    aliquot_sum: int = sum(factors(number))
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    elif aliquot_sum < number:
        return "deficient"


def factors(number: int) -> [int]:
    """ Calculates all the factors of the given number (not including the number itself)
    :param number: int - a positive integer
    :return :[int] - list of all factors for a givet number
    """
    return [x for x in range(1, number // 2 + 1) if number % x == 0]
