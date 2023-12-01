import re


def calculate_calilbration(input: [str]):
    sum = 0
    for line in input:
        line = filter_non_digits(line)
        first_digit = line[0]
        last_digit = line[-1]
        sum = sum + int(first_digit + last_digit)
    return sum


def filter_non_digits(string):
    return re.sub(r"[^\d]", "", string)


# -----------------

def calculate_calilbration_2(input: [str]):
    sum = 0
    for line in input:
        line = replace_words_to_digits(line)
        line = filter_non_digits(line)
        first_digit = line[0]
        last_digit = line[-1]
        sum = sum + int(first_digit + last_digit)
    return sum


def replace_words_to_digits(line):
    digits = [
        ("zerone", "01"),
        ("oneight", "18"),
        ("twone", "21"),
        ("threeight", "38"),
        ("fiveight", "58"),
        ("eightwo", "82"),
        ("zero", "0"),
        ("one", "1"),
        ("two", "2"),
        ("three", "3"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9"),
    ]
    for tran in digits:
        line = re.sub(tran[0], tran[1], line)
    return line
