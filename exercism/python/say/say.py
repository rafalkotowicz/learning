def parse_3_digits(number: int) -> str:
    int_to_word = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety'
    }

    result: str = ""
    hundred: int = number // 100
    tens: int = (number - hundred * 100) // 10
    digit: int = number % 10

    if hundred > 0:
        result += f"{int_to_word[hundred]} hundred "
    if tens > 0:
        if tens == 1:
            result += f"{int_to_word[tens * 10 + digit]}"
            return result
        else:
            if digit != 0:
                result += f"{int_to_word[tens * 10]}-"
            else:
                result += f"{int_to_word[tens * 10]}"
                return result
    if digit > 0:
        result += f"{int_to_word[digit]}"

    return result.strip()


def say(number: int) -> str:
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")
    if number == 0:
        return "zero"

    result: str = ""
    billions: int = number // 1_000_000_000
    millions: int = (number - billions * 1_000_000_000) // 1_000_000
    thousands: int = (number - billions * 1_000_000_000 - millions * 1_000_000) // 1_000
    if billions > 0:
        result += f"{parse_3_digits(billions)} billion "
    if millions > 0:
        result += f"{parse_3_digits(millions)} million "
    if thousands > 0:
        result += f"{parse_3_digits(thousands)} thousand "
    if number % 1_000 > 0:
        result += f"{parse_3_digits(number % 1_000)}"

    return result.strip()
