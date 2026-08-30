"""Compute degree of separation in a family tree."""

from collections import deque
from itertools import combinations


class RelativeDistance:  # pylint: disable=too-few-public-methods
    """Provide shortest relationship distance between two individuals."""

    def __init__(self, family_tree: dict[str, list[str]]) -> None:
        self._all_people: set[str] = set()
        self._relationships: dict[str, set[str]] = {}

        for parent_name, children_names in family_tree.items():
            self._all_people.add(parent_name)
            self._relationships.setdefault(parent_name, set())

            for child_name in children_names:
                self._all_people.add(child_name)
                self._relationships.setdefault(child_name, set())

                self._relationships[parent_name].add(child_name)
                self._relationships[child_name].add(parent_name)

            for first_sibling, second_sibling in combinations(children_names, 2):
                self._relationships[first_sibling].add(second_sibling)
                self._relationships[second_sibling].add(first_sibling)

    def degree_of_separation(self, person_a: str, person_b: str) -> int:
        """Return the shortest relationship distance between two people."""
        if person_a not in self._all_people:
            raise ValueError("Person A not in family tree.")

        if person_b not in self._all_people:
            raise ValueError("Person B not in family tree.")

        if person_a == person_b:
            return 0

        pending_people: deque[tuple[str, int]] = deque([(person_a, 0)])
        visited_people: set[str] = {person_a}

        while pending_people:
            current_person, current_distance = pending_people.popleft()

            for related_person in self._relationships.get(current_person, set()):
                if related_person in visited_people:
                    continue

                next_distance = current_distance + 1
                if related_person == person_b:
                    return next_distance

                visited_people.add(related_person)
                pending_people.append((related_person, next_distance))

        raise ValueError("No connection between person A and person B.")
