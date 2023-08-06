color_digits: dict() = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

color_tolerance: dict() = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10
}


def compute_ohm_value(colors: [str]) -> int:
    if len(colors) == 1:
        return color_digits[colors[0]]
    elif len(colors) == 4:
        return (color_digits[colors[0]] * 10 + color_digits[colors[1]]) * 10 ** color_digits[colors[2]]
    else:
        return (color_digits[colors[0]] * 100 + color_digits[colors[1]] * 10 + color_digits[colors[2]]) * 10 ** \
            color_digits[colors[3]]


def compute_prefix(ohm_value: int) -> (str, int):
    if ohm_value < 1_000:
        return "", ohm_value
    elif ohm_value < 1_000_000:
        if ohm_value % 1_000 == 0:
            return "kilo", ohm_value // 1_000
        else:
            return "kilo", ohm_value / 1_000
    else:
        if ohm_value % 1_000_000 == 0:
            return "mega", ohm_value // 1_000_000
        else:
            return "mega", ohm_value / 1_000_000


def compute_tolerance(colors: [str]) -> str:
    if len(colors) == 1:
        return ""
    else:
        return f" ±{color_tolerance[colors[-1]]}%"


def resistor_label(colors: [str]) -> str:
    ohm_value: int = compute_ohm_value(colors)
    unit_prefix, ohm_value = compute_prefix(ohm_value)
    tolerance: str = compute_tolerance(colors)
    return f"{ohm_value} {unit_prefix}ohms{tolerance}"
