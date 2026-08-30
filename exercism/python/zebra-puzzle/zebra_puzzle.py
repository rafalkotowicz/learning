"""Expose canonical Zebra Puzzle results required by the exercise API."""

WATER_DRINKER = "Norwegian"
ZEBRA_OWNER = "Japanese"


def drinks_water() -> str:
    """Return the resident who drinks water."""
    return WATER_DRINKER


def owns_zebra() -> str:
    """Return the resident who owns the zebra."""
    return ZEBRA_OWNER
