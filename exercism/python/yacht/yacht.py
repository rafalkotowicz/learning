from collections import Counter

YACHT = (lambda x: 50 if len(set(x)) == 1 else 0)
ONES = (lambda x: sum_of_digits(x, 1))
TWOS = (lambda x: sum_of_digits(x, 2))
THREES = (lambda x: sum_of_digits(x, 3))
FOURS = (lambda x: sum_of_digits(x, 4))
FIVES = (lambda x: sum_of_digits(x, 5))
SIXES = (lambda x: sum_of_digits(x, 6))
FULL_HOUSE = (lambda x: sum(x) if sorted(Counter(x).values()) == [2, 3] else 0)
FOUR_OF_A_KIND = (lambda x: four_of_a_kind(x))
LITTLE_STRAIGHT = (lambda x: 30 if sorted(x) == [1, 2, 3, 4, 5] else 0)
BIG_STRAIGHT = (lambda x: 30 if sorted(x) == [2, 3, 4, 5, 6] else 0)
CHOICE = sum


def sum_of_digits(x: list[int], digit):
    return x.count(digit) * digit


def four_of_a_kind(x):
    four_time_digit = [dice for dice in set(x) if x.count(dice) >= 4]
    return 4 * four_time_digit[0] if len(four_time_digit) > 0 else 0


def score(dices: [int], category) -> int:
    return category(dices)
