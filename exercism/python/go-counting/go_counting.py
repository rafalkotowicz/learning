"""Go Counting exercise solution."""

from collections import deque

WHITE = "W"
BLACK = "B"
NONE = ""
EMPTY = " "
COORDINATE_KEY_COLUMN = "x"
COORDINATE_KEY_ROW = "y"


class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self._board = board
        self._height = len(board)
        self._width = len(board[0]) if board else 0

    def _validate_coordinate(self, column_index, row_index):
        if (
            column_index < 0
            or row_index < 0
            or column_index >= self._width
            or row_index >= self._height
        ):
            raise ValueError("Invalid coordinate")

    def _neighbors(self, coordinate):
        coordinate_x, coordinate_y = coordinate
        for delta_x, delta_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            neighbor_x = coordinate_x + delta_x
            neighbor_y = coordinate_y + delta_y
            if 0 <= neighbor_x < self._width and 0 <= neighbor_y < self._height:
                yield neighbor_x, neighbor_y

    def _char_at(self, coordinate):
        coordinate_x, coordinate_y = coordinate
        return self._board[coordinate_y][coordinate_x]

    def _empty_region_owner_and_points(self, start_coordinate):
        queue = deque([start_coordinate])
        region_points = {start_coordinate}
        bordering_stones = set()

        while queue:
            current_coordinate = queue.popleft()
            for neighbor_coordinate in self._neighbors(current_coordinate):
                neighbor_char = self._char_at(neighbor_coordinate)
                if neighbor_char == EMPTY and neighbor_coordinate not in region_points:
                    region_points.add(neighbor_coordinate)
                    queue.append(neighbor_coordinate)
                elif neighbor_char in (BLACK, WHITE):
                    bordering_stones.add(neighbor_char)

        if len(bordering_stones) == 1:
            owner = next(iter(bordering_stones))
            return owner, region_points

        return NONE, region_points

    def territory(self, column_index=None, row_index=None, **named_coordinates):
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            column_index (int): Column on the board
            row_index (int): Row on the board
            named_coordinates (dict): Optional keyword coordinates, e.g. x and y.

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        # Keep compatibility with territory(x=..., y=...) keyword calls.
        if column_index is None and COORDINATE_KEY_COLUMN in named_coordinates:
            column_index = named_coordinates[COORDINATE_KEY_COLUMN]
        if row_index is None and COORDINATE_KEY_ROW in named_coordinates:
            row_index = named_coordinates[COORDINATE_KEY_ROW]

        self._validate_coordinate(column_index, row_index)

        coordinate = (column_index, row_index)
        if self._char_at(coordinate) != EMPTY:
            return NONE, set()

        return self._empty_region_owner_and_points(coordinate)

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        all_territories = {BLACK: set(), WHITE: set(), NONE: set()}
        visited_coordinates = set()

        for row_index in range(self._height):
            for column_index in range(self._width):
                coordinate = (column_index, row_index)
                if coordinate in visited_coordinates or self._char_at(coordinate) != EMPTY:
                    continue

                owner, region_points = self._empty_region_owner_and_points(coordinate)
                visited_coordinates.update(region_points)
                all_territories[owner].update(region_points)

        return all_territories
