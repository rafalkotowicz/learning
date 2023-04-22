def label(colors: list[str]) -> str:
    translated: list[int] = list(map(color_code, colors))
    d1, d2, zeros, *ignore_more_input = translated
    number: int = d1 * 10 ** (zeros + 1) + d2 * 10 ** zeros
    return print_resistance(number)


def print_resistance(val: int) -> str:
    if val == 0:
        return "0 ohms"

    if val % 1_000_000_000 == 0:
        return str(val // 1_000_000_000) + " gigaohms"
    elif val % 1_000_000 == 0:
        return str(val // 1_000_000) + " megaohms"
    elif val % 1_000 == 0:
        return str(val // 1_000) + " kiloohms"
    else:
        return str(val) + " ohms"


def color_code(color: str) -> int:
    """
    Translate resistor color to integer value
    @type color: resistor color
    @return int: integer value
    """
    if color == "black":
        return 0
    elif color == "brown":
        return 1
    elif color == "red":
        return 2
    elif color == "orange":
        return 3
    elif color == "yellow":
        return 4
    elif color == "green":
        return 5
    elif color == "blue":
        return 6
    elif color == "violet":
        return 7
    elif color == "grey":
        return 8
    elif color == "white":
        return 9
