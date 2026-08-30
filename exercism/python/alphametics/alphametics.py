"""Solver for the Exercism alphametics exercise."""

from __future__ import annotations

DIGIT_BASE = 10


class AlphameticsSolver:
    """Solve a single alphametics equation."""

    def __init__(self, puzzle: str) -> None:
        """Parse and initialize puzzle state used during backtracking."""
        left_side, right_side = puzzle.split(" == ")
        self.addend_words = left_side.split(" + ")
        self.result_word = right_side
        self.leading_letters = {
            word_value[0]
            for word_value in self.addend_words + [self.result_word]
            if len(word_value) > 1
        }
        self.assignments: dict[str, int] = {}
        self.used_digits: set[int] = set()
        self.addend_count = len(self.addend_words)

    def has_too_many_letters(self) -> bool:
        """Return True when puzzle cannot fit into decimal digits."""
        unique_letters = set("".join(self.addend_words) + self.result_word)
        return len(unique_letters) > DIGIT_BASE

    def candidate_digits(self, letter_symbol: str) -> list[int]:
        """Return currently available digits for a given letter."""
        start_digit = 1 if letter_symbol in self.leading_letters else 0
        return [
            digit_value
            for digit_value in range(start_digit, DIGIT_BASE)
            if digit_value not in self.used_digits
        ]

    def solve(self) -> dict[str, int] | None:
        """Try to solve puzzle and return a full assignments mapping."""
        if not self.solve_addends_for_column(0, 0, 0):
            return None
        return self.assignments.copy()

    def solve_addends_for_column(
        self, column_index: int, addend_index: int, column_total: int
    ) -> bool:
        """Recursively process all addends for one digit column."""
        if addend_index == self.addend_count:
            return self.solve_result_for_column(column_index, column_total)

        addend_word = self.addend_words[addend_index]
        if column_index >= len(addend_word):
            return self.solve_addends_for_column(column_index, addend_index + 1, column_total)

        letter_symbol = addend_word[-1 - column_index]
        if (assigned_digit := self.assignments.get(letter_symbol)) is not None:
            return self.solve_addends_for_column(
                column_index, addend_index + 1, column_total + assigned_digit
            )

        for digit_value in self.candidate_digits(letter_symbol):
            self.assignments[letter_symbol] = digit_value
            self.used_digits.add(digit_value)

            solved = self.solve_addends_for_column(
                column_index, addend_index + 1, column_total + digit_value
            )
            if solved:
                return True

            self.used_digits.remove(digit_value)
            del self.assignments[letter_symbol]

        return False

    def solve_result_for_column(self, column_index: int, column_total: int) -> bool:
        """Validate or assign the result digit for the current column."""
        if column_index >= len(self.result_word):
            return not column_total

        result_letter = self.result_word[-1 - column_index]
        expected_digit = column_total % DIGIT_BASE
        next_carry = column_total // DIGIT_BASE

        if (assigned_digit := self.assignments.get(result_letter)) is not None:
            matches_expected = assigned_digit == expected_digit
            return matches_expected and self.solve_addends_for_column(
                column_index + 1, 0, next_carry
            )

        if expected_digit in self.used_digits:
            return False
        if not expected_digit and result_letter in self.leading_letters:
            return False

        self.assignments[result_letter] = expected_digit
        self.used_digits.add(expected_digit)

        if solved := self.solve_addends_for_column(column_index + 1, 0, next_carry):
            return solved

        self.used_digits.remove(expected_digit)
        del self.assignments[result_letter]
        return False


def solve(puzzle: str) -> dict[str, int] | None:
    """Return a mapping letter->digit that satisfies the alphametics puzzle."""
    solver = AlphameticsSolver(puzzle)
    if solver.has_too_many_letters():
        return None
    return solver.solve()
