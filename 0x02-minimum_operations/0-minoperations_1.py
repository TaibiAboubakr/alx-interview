#!/usr/bin/python3
""" min operations """


def prime_factors(n: int) -> dict:
    """ prime factors """
    factors = {}
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            if divisor in factors:
                factors[divisor] += 1
            else:
                factors[divisor] = 1
            n //= divisor
        divisor += 1
    return factors


def minOperations(n: int) -> int:
    """min operations  """
    return sum(key * val for key, val in list(prime_factors(n).items())[:])
