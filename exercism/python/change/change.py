"""Change exercise implementation."""

NEGATIVE_TARGET_MESSAGE = "target can't be negative"
IMPOSSIBLE_TARGET_MESSAGE = "can't make target with given coins"


def find_fewest_coins(coins, target) -> list[int]:
    """Return the fewest coins that sum to target, or raise ValueError if impossible."""
    if target < 0:
        raise ValueError(NEGATIVE_TARGET_MESSAGE)
    if not target:
        return []

    fewest_coins_by_amount = [None] * (target + 1)
    fewest_coins_by_amount[0] = []

    for amount in range(1, target + 1):
        best_combo = None

        for coin in coins:
            if coin <= 0 or coin > amount or fewest_coins_by_amount[amount - coin] is None:
                continue

            candidate = fewest_coins_by_amount[amount - coin] + [coin]

            if best_combo is None or len(candidate) < len(best_combo):
                best_combo = candidate

        fewest_coins_by_amount[amount] = best_combo

    if fewest_coins_by_amount[target] is None:
        raise ValueError(IMPOSSIBLE_TARGET_MESSAGE)

    return sorted(fewest_coins_by_amount[target])
