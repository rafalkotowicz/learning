def roman(number: int) -> str:
    thousands: int = number // 1000
    hundreds: int = (number - thousands * 1000) // 100
    tens: int = (number - thousands * 1000 - hundreds * 100) // 10
    other: int = number % 10
    roman_number: str = ""

    if thousands:
        roman_number += build_element(thousands, ["M", "M", "M"])
    if hundreds:
        roman_number += build_element(hundreds, ["C", "D", "M"])
    if tens:
        roman_number += build_element(tens, ["X", "L", "C"])
    if other:
        roman_number += build_element(other, ["I", "V", "X"])

    return roman_number


def build_element(digit, roman_digits: [str]) -> str:
    low, mid, high = roman_digits
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
