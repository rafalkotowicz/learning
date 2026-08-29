"""Flower Field exercise implementation."""

FLOWER = "*"
EMPTY = " "
INVALID_BOARD_MESSAGE = "The board is invalid with current input."
NEIGHBOR_OFFSETS = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)


def _validate_garden(garden):
    """Validate garden dimensions and characters."""
    expected_width = len(garden[0])

    for row in garden:
        if len(row) != expected_width:
            raise ValueError(INVALID_BOARD_MESSAGE)
        if any(cell not in (EMPTY, FLOWER) for cell in row):
            raise ValueError(INVALID_BOARD_MESSAGE)


def _count_neighboring_flowers(garden, row_index, column_index):
    """Return the number of neighboring flowers for a given cell."""
    height = len(garden)
    width = len(garden[0])
    neighbors = 0

    for row_offset, column_offset in NEIGHBOR_OFFSETS:
        neighbor_row = row_index + row_offset
        neighbor_column = column_index + column_offset

        if 0 <= neighbor_row < height and 0 <= neighbor_column < width:
            if garden[neighbor_row][neighbor_column] == FLOWER:
                neighbors += 1

    return neighbors


def annotate(garden):
    """Return garden rows with empty squares replaced by neighboring flower counts."""
    if not garden:
        return []

    _validate_garden(garden)
    result = []

    for row_index, row in enumerate(garden):
        annotated_row = []

        for column_index, cell in enumerate(row):
            if cell == FLOWER:
                annotated_row.append(FLOWER)
                continue

            neighbors = _count_neighboring_flowers(garden, row_index, column_index)

            annotated_row.append(str(neighbors) if neighbors else EMPTY)

        result.append("".join(annotated_row))

    return result
