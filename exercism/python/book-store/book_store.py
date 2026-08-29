"""Book Store exercise implementation."""

from functools import lru_cache
from math import inf

BOOK_PRICE_BY_GROUP_SIZE = {
    1: 800,
    2: 1520,
    3: 2160,
    4: 2560,
    5: 3000,
}
TITLE_IDS = (1, 2, 3, 4, 5)


def total(basket):
    """Return the minimum basket price (in cents) with optimal grouping discounts."""
    counts = tuple(basket.count(title_id) for title_id in TITLE_IDS)

    @lru_cache(maxsize=None)
    def cheapest_price(state):
        if not any(state):
            return 0

        best = inf

        for subset_mask in range(1, 1 << len(TITLE_IDS)):
            next_state = list(state)
            group_size = 0
            valid_subset = True

            for index in range(len(TITLE_IDS)):
                if (subset_mask >> index) & 1:
                    if not next_state[index]:
                        valid_subset = False
                        break
                    next_state[index] -= 1
                    group_size += 1

            if not valid_subset:
                continue

            candidate = BOOK_PRICE_BY_GROUP_SIZE[group_size] + cheapest_price(tuple(next_state))
            best = min(best, candidate)

        return int(best)

    return cheapest_price(counts)
