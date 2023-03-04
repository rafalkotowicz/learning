def roman(number: int) -> str:
    thousands: int = number // 1000
    hundreds: int = (number - thousands * 1000) // 100
    tens: int = (number - thousands * 1000 - hundreds * 100) // 10
    other: int = number % 10
    roman_number: str = ""

    if thousands:
        roman_number += translate_one_digit_to_roman(thousands, ["M", "M", "M"])
    if hundreds:
        roman_number += translate_one_digit_to_roman(hundreds, ["C", "D", "M"])
    if tens:
        roman_number += translate_one_digit_to_roman(tens, ["X", "L", "C"])
    if other:
        roman_number += translate_one_digit_to_roman(other, ["I", "V", "X"])

    return roman_number


def translate_one_digit_to_roman(digit, roman_chars: [str]) -> str:
    low, mid, high = roman_chars
    roman_number_part: str = ""
    if digit in [1, 2, 3]:
        roman_number_part += low * digit
    elif digit == 4:
        roman_number_part += low + mid
    elif digit == 5:
        roman_number_part += mid
    elif digit in [6, 7, 8]:
        roman_number_part += mid + (digit - 5) * low
    elif digit == 9:
        roman_number_part += low + high

    return roman_number_part
