"""Determine the winner on a hex-grid Connect board."""

from collections import deque


class ConnectGame:  # pylint: disable=too-few-public-methods
    """Represent a Connect board and compute its winner."""

    PLAYER_X = "X"
    PLAYER_O = "O"

    def __init__(self, board: str) -> None:
        self.grid: list[list[str]] = self._parse_board(board)
        self.row_count: int = len(self.grid)
        self.column_count: int = len(self.grid[0]) if self.grid else 0

    def get_winner(self) -> str:
        """Return the winner marker or an empty string when no player has won."""
        if self._has_winning_path(self.PLAYER_X):
            return self.PLAYER_X
        if self._has_winning_path(self.PLAYER_O):
            return self.PLAYER_O
        return ""

    @staticmethod
    def _parse_board(board: str) -> list[list[str]]:
        """Parse the string board into rows and columns without indentation spaces."""
        rows: list[list[str]] = []
        for raw_row in board.splitlines():
            if not (stripped_row := raw_row.strip()):
                continue
            rows.append(stripped_row.split())
        return rows

    def _has_winning_path(self, player_mark: str) -> bool:
        """Check whether the selected player has a full path to the opposite edge."""
        search_queue: deque[tuple[int, int]] = deque()
        visited_positions: set[tuple[int, int]] = set()

        if not self.row_count or not self.column_count:
            return False

        starting_positions = self._starting_positions(player_mark)
        for position in starting_positions:
            search_queue.append(position)
            visited_positions.add(position)

        while search_queue:
            row_index, column_index = search_queue.popleft()
            if self._is_target_edge(player_mark, row_index, column_index):
                return True

            for neighbor_row, neighbor_column in self._neighbors(row_index, column_index):
                if (neighbor_position := (neighbor_row, neighbor_column)) in visited_positions:
                    continue
                if self.grid[neighbor_row][neighbor_column] != player_mark:
                    continue
                visited_positions.add(neighbor_position)
                search_queue.append(neighbor_position)

        return False

    def _starting_positions(self, player_mark: str) -> list[tuple[int, int]]:
        """Collect all board coordinates where path search should start for a player."""
        if player_mark == self.PLAYER_X:
            return [
                (row_index, 0)
                for row_index in range(self.row_count)
                if self.grid[row_index][0] == player_mark
            ]
        return [
            (0, column_index)
            for column_index in range(self.column_count)
            if self.grid[0][column_index] == player_mark
        ]

    def _is_target_edge(self, player_mark: str, row_index: int, column_index: int) -> bool:
        """Return whether the current coordinate reached the player's destination edge."""
        if player_mark == self.PLAYER_X:
            return column_index == self.column_count - 1
        return row_index == self.row_count - 1

    def _neighbors(self, row_index: int, column_index: int) -> list[tuple[int, int]]:
        """Yield legal hex-grid neighbors for a coordinate."""
        offsets: list[tuple[int, int]] = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0)]
        adjacent_positions: list[tuple[int, int]] = []

        for row_offset, column_offset in offsets:
            next_row = row_index + row_offset
            next_column = column_index + column_offset
            if 0 <= next_row < self.row_count and 0 <= next_column < self.column_count:
                adjacent_positions.append((next_row, next_column))

        return adjacent_positions
