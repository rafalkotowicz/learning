def square_of_sum(number: int) -> int:
    sum = 0
    for x in range(1, number + 1):
        sum += x
    return sum ** 2


def sum_of_squares(number: int) -> int:
    sum_of_sqrs = 0
    for x in range(1, number + 1):
        sum_of_sqrs += x ** 2
    return sum_of_sqrs


def difference_of_squares(number: int) -> int:
    return square_of_sum(number) - sum_of_squares(number)
