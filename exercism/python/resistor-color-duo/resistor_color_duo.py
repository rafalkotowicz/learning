def color_code(color: str) -> int:
    """
    Translate resistor color to resistance value
    @type color: resistor color
    @return int: resistance value
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


def value(colors: list[str]) -> int:
    translated = []
    for color in colors:
        translated.append(color_code(color))
    return translated[0:2][0] * 10 + translated[0:2][1]
