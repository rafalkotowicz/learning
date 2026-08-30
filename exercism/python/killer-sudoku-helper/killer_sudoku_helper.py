"""Helpers for finding valid Killer Sudoku cage combinations."""


def combinations(target: int, size: int, exclude: list[int]) -> list[list[int]]:
    """Return ascending unique digit combinations that sum to target."""
    excluded_digits: set[int] = set(exclude)
    all_combinations: list[list[int]] = []

    def build_combinations(
        next_digit: int,
        remaining_sum: int,
        remaining_slots: int,
        selected_digits: list[int],
    ) -> None:
        if not remaining_slots:
            if not remaining_sum:
                all_combinations.append(selected_digits.copy())
            return

        for candidate_digit in range(next_digit, 10):
            if candidate_digit in excluded_digits:
                continue
            if candidate_digit > remaining_sum:
                break

            selected_digits.append(candidate_digit)
            build_combinations(
                candidate_digit + 1,
                remaining_sum - candidate_digit,
                remaining_slots - 1,
                selected_digits,
            )
            selected_digits.pop()

    build_combinations(1, target, size, [])
    return all_combinations
