"""State of Tic-Tac-Toe exercise implementation."""

MARK_CROSS = "X"
MARK_NOUGHT = "O"
EMPTY_CELL = " "
STATE_WIN = "win"
STATE_DRAW = "draw"
STATE_ONGOING = "ongoing"

ERROR_CROSS_WENT_TWICE = "Wrong turn order: X went twice"
ERROR_NOUGHT_STARTED = "Wrong turn order: O started"
ERROR_IMPOSSIBLE_BOARD = "Impossible board: game should have ended after the game was won"


def _winning_lines(board):
    """Return all row, column, and diagonal lines from a board."""
    lines = list(board)

    for column_index in range(3):
        lines.append("".join(board[row_index][column_index] for row_index in range(3)))

    lines.append("".join(board[index][index] for index in range(3)))
    lines.append("".join(board[index][2 - index] for index in range(3)))
    return lines


def _has_winning_line(board, mark):
    """Return True when a mark has any winning line."""
    winning_pattern = mark * 3
    return any(line == winning_pattern for line in _winning_lines(board))


def gamestate(board):
    """Return game state as 'win', 'draw' or 'ongoing', or raise ValueError."""
    cross_count = sum(row.count(MARK_CROSS) for row in board)

    if (nought_count := sum(row.count(MARK_NOUGHT) for row in board)) > cross_count:
        raise ValueError(ERROR_NOUGHT_STARTED)
    if cross_count > nought_count + 1:
        raise ValueError(ERROR_CROSS_WENT_TWICE)

    cross_won = _has_winning_line(board, MARK_CROSS)
    nought_won = _has_winning_line(board, MARK_NOUGHT)

    if cross_won and nought_won:
        raise ValueError(ERROR_IMPOSSIBLE_BOARD)
    if cross_won and cross_count != nought_count + 1:
        raise ValueError(ERROR_IMPOSSIBLE_BOARD)
    if nought_won and cross_count != nought_count:
        raise ValueError(ERROR_IMPOSSIBLE_BOARD)

    if cross_won or nought_won:
        return STATE_WIN

    if any(EMPTY_CELL in row for row in board):
        return STATE_ONGOING

    return STATE_DRAW
