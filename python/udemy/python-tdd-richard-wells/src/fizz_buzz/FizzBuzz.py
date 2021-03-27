# Requirement:
# Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number
# and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

def fizz_buzz(value):
    if is_multiple(value, 15):
        return 'FizzBuzz'
    if is_multiple(value, 5):
        return 'Buzz'
    if is_multiple(value, 3):
        return 'Fizz'
    return value


def is_multiple(value, mod):
    return value % mod == 0


def printer(numbers):
    transformed = list()
    for number in numbers:
        transformed.append(str(fizz_buzz(number)))
    return "".join(transformed)
