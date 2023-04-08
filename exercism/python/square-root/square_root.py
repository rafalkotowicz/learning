import math


def square_root(number):
    guess = 0
    while math.fabs(guess**2 - number) >= 0.001:
        guess += 0.1

    return round(guess)
