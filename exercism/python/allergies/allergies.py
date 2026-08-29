"""Allergies exercise implementation."""


class Allergies:
    """Represent allergies encoded in an integer score."""

    _ALLERGENS = (
        "eggs",
        "peanuts",
        "shellfish",
        "strawberries",
        "tomatoes",
        "chocolate",
        "pollen",
        "cats",
    )
    _VALID_BITS_MASK = 0xFF

    def __init__(self, score):
        """Store only score bits that map to known allergens."""
        self._score = score & self._VALID_BITS_MASK

    def allergic_to(self, item):
        """Return True when the encoded score contains the given allergen."""
        if item not in self._ALLERGENS:
            return False

        allergen_index = self._ALLERGENS.index(item)
        allergen_value = 1 << allergen_index
        return bool(self._score & allergen_value)

    @property
    def lst(self):
        """Return all allergens present in the encoded score."""
        return [
            allergen
            for allergen_index, allergen in enumerate(self._ALLERGENS)
            if self._score & (1 << allergen_index)
        ]
