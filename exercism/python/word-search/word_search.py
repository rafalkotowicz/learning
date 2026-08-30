"""Word Search solver for finding words in 8 directions on a letter grid."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    """Represents a coordinate in the puzzle grid."""

    column_index: int
    row_index: int


class WordSearch:  # pylint: disable=too-few-public-methods
    """Searches words in horizontal, vertical and diagonal directions."""

    def __init__(self, puzzle: list[str]) -> None:
        self._grid = puzzle
        self._row_count = len(puzzle)
        self._column_count = len(puzzle[0]) if puzzle else 0

    def search(self, word: str) -> tuple[Point, Point] | None:
        """Return start/end coordinates for a word, or None when not found."""
        if not word:
            return None

        direction_vectors: tuple[tuple[int, int], ...] = (
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (1, 1),
            (-1, -1),
            (1, -1),
            (-1, 1),
        )

        for row_index in range(self._row_count):
            for column_index in range(self._column_count):
                for vector_column, vector_row in direction_vectors:
                    match_result = self._match_from_position(
                        word,
                        start_column=column_index,
                        start_row=row_index,
                        step_column=vector_column,
                        step_row=vector_row,
                    )
                    if match_result is not None:
                        return match_result

        return None

    def _match_from_position(
        self,
        word: str,
        start_column: int,
        start_row: int,
        step_column: int,
        step_row: int,
    ) -> tuple[Point, Point] | None:
        last_column = start_column + (len(word) - 1) * step_column
        last_row = start_row + (len(word) - 1) * step_row

        if not self._is_inside_grid(last_column, last_row):
            return None

        for letter_index, expected_letter in enumerate(word):
            current_column = start_column + letter_index * step_column
            current_row = start_row + letter_index * step_row
            if self._grid[current_row][current_column] != expected_letter:
                return None

        return Point(start_column, start_row), Point(last_column, last_row)

    def _is_inside_grid(self, column_index: int, row_index: int) -> bool:
        return (
            0 <= row_index < self._row_count
            and 0 <= column_index < self._column_count
        )
