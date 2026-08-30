"""Custom Set exercise implementation."""

from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import Any


class CustomSet:
    """A minimal mutable set implementation with unique elements."""

    __hash__ = None

    def __init__(self, elements: Iterable[Any] | None = None) -> None:
        """Create a set from optional iterable input."""
        if elements is None:
            self._elements: set[Any] = set()
        else:
            self._elements = set(elements)

    def values(self) -> Iterator[Any]:
        """Yield all values stored in this set."""
        return iter(self._elements)

    def isempty(self) -> bool:
        """Return True when the set has no elements."""
        return not self._elements

    def __contains__(self, element: Any) -> bool:
        """Return True when an element is present in the set."""
        return element in self._elements

    def issubset(self, other: CustomSet) -> bool:
        """Return True when all elements of this set exist in the other set."""
        return all(element in other for element in self._elements)

    def isdisjoint(self, other: CustomSet) -> bool:
        """Return True when two sets share no elements."""
        return all(element not in other for element in self._elements)

    def __eq__(self, other: object) -> bool:
        """Compare two sets by their contained unique elements."""
        if not isinstance(other, CustomSet):
            return NotImplemented
        return self.issubset(other) and other.issubset(self)

    def add(self, element: Any) -> None:
        """Add an element to the set."""
        self._elements.add(element)

    def intersection(self, other: CustomSet) -> CustomSet:
        """Return a set containing only shared elements."""
        return CustomSet(element for element in self._elements if element in other)

    def __sub__(self, other: CustomSet) -> CustomSet:
        """Return a set with elements from this set that are not in the other set."""
        return CustomSet(element for element in self._elements if element not in other)

    def __add__(self, other: CustomSet) -> CustomSet:
        """Return the union of this set and the other set."""
        result_set = CustomSet(self._elements)
        for element in other.values():
            result_set.add(element)
        return result_set
