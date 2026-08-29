"""Generate prime numbers up to a provided limit using the Sieve of Eratosthenes."""


MIN_PRIME = 2


def primes(limit):
    """Return all prime numbers less than or equal to ``limit``."""
    if limit < MIN_PRIME:
        return []

    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False

    candidate = MIN_PRIME
    while candidate * candidate <= limit:
        if is_prime[candidate]:
            for multiple in range(candidate * candidate, limit + 1, candidate):
                is_prime[multiple] = False
        candidate += 1

    return [number for number, prime in enumerate(is_prime) if prime]
