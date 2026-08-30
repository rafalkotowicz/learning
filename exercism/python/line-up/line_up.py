"""Format customer order using the correct English ordinal suffix."""

SPECIAL_CASE_START = 11
SPECIAL_CASE_END = 13
TENS_BASE = 10
HUNDREDS_BASE = 100
FIRST_POSITION_REMAINDER = 1
SECOND_POSITION_REMAINDER = 2
THIRD_POSITION_REMAINDER = 3


def line_up(name: str, number: int) -> str:
    """Return a polite sentence including the customer's ordinal number."""
    suffix = _ordinal_suffix(number)
    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"


def _ordinal_suffix(number: int) -> str:
    """Return the ordinal suffix for the provided integer."""
    last_two_digits = number % HUNDREDS_BASE
    if SPECIAL_CASE_START <= last_two_digits <= SPECIAL_CASE_END:
        return "th"

    last_digit = number % TENS_BASE
    if last_digit == FIRST_POSITION_REMAINDER:
        return "st"
    if last_digit == SECOND_POSITION_REMAINDER:
        return "nd"
    if last_digit == THIRD_POSITION_REMAINDER:
        return "rd"
    return "th"
