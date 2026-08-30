"""Compute the maximum obtainable value for a 0/1 knapsack instance."""

from collections.abc import Mapping, Sequence


def maximum_value(maximum_weight: int, items: Sequence[Mapping[str, int]]) -> int:
    """Return the highest value achievable within the given weight capacity."""
    best_values_by_capacity = [0] * (maximum_weight + 1)

    for item in items:
        item_weight = item["weight"]
        item_value = item["value"]

        if item_weight > maximum_weight:
            continue

        # Iterate capacities backward to avoid reusing the same item.
        for current_capacity in range(maximum_weight, item_weight - 1, -1):
            value_with_item = (
                best_values_by_capacity[current_capacity - item_weight] + item_value
            )
            best_values_by_capacity[current_capacity] = max(
                best_values_by_capacity[current_capacity], value_with_item
            )

    return best_values_by_capacity[maximum_weight]
