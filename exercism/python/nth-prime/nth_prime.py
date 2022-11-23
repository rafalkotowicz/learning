import math


def is_prime(number: int) -> bool:
    i: int = 2
    # while i <= number / 2:
    while i <= math.sqrt(number):
        if number % i != 0:
            i += 1
            continue
        else:
            return False
    return True


def prime(nth_prime: int) -> int:
    if nth_prime == 0:
        raise ValueError("there is no zeroth prime")

    primes: [int] = []
    number: int = 2
    while len(primes) < nth_prime:
        if is_prime(number):
            primes.append(number)
        number += 1

    return primes[-1]
