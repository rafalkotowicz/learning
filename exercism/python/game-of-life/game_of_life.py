"""Conway's Game of Life implementation."""

SURVIVAL_NEIGHBORS = {2, 3}
REPRODUCTION_NEIGHBORS = 3


def tick(matrix):
    """Return the next generation matrix based on Conway's rules."""
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    next_matrix = [[0 for col_index in range(cols)] for row_index in range(rows)]

    for row in range(rows):
        for col in range(cols):
            live_neighbors = 0

            for row_delta in (-1, 0, 1):
                for col_delta in (-1, 0, 1):
                    if not row_delta and not col_delta:
                        continue

                    neighbor_row = row + row_delta
                    neighbor_col = col + col_delta

                    if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                        live_neighbors += matrix[neighbor_row][neighbor_col]

            cell = matrix[row][col]
            if cell == 1 and live_neighbors in SURVIVAL_NEIGHBORS:
                next_matrix[row][col] = 1
            elif not cell and live_neighbors == REPRODUCTION_NEIGHBORS:
                next_matrix[row][col] = 1

    return next_matrix
