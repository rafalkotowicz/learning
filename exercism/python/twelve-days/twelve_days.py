"""Twelve Days exercise implementation."""

ORDINAL_DAYS = (
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
)

GIFTS_BY_DAY = (
    "a Partridge in a Pear Tree.",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming",
)


def _gifts_phrase(day_number):
    """Return cumulative gifts phrase for a given day number."""
    if day_number == 1:
        return GIFTS_BY_DAY[0]

    gifts = [GIFTS_BY_DAY[index] for index in range(day_number - 1, 0, -1)]
    gifts.append(f"and {GIFTS_BY_DAY[0]}")
    return ", ".join(gifts)


def recite(start_verse, end_verse):
    """Return selected verses from The Twelve Days of Christmas."""
    verses = []

    for day_number in range(start_verse, end_verse + 1):
        day_name = ORDINAL_DAYS[day_number - 1]
        gifts_phrase = _gifts_phrase(day_number)
        verses.append(
            f"On the {day_name} day of Christmas my true love gave to me: {gifts_phrase}"
        )

    return verses
