def spiral_matrix(size):
    matrix: [[int]] = [[0 for i in range(size)] for j in range(size)]
    if 0 == size:
        return matrix

    y = 0
    x = 0
    matrix[0][0] = 1
    sequence_generator = number_sequence(2, size ** 2, 1)

    while (has_zero(matrix)):
        # go right
        while is_inbound(x + 1, y, size) and matrix[y][x + 1] == 0:
            x = x + 1
            matrix[y][x] = next(sequence_generator)

        # go down
        while is_inbound(x, y + 1, size) and matrix[y + 1][x] == 0:
            y = y + 1
            matrix[y][x] = next(sequence_generator)

        # go left
        while is_inbound(x - 1, y, size) and matrix[y][x - 1] == 0:
            x = x - 1
            matrix[y][x] = next(sequence_generator)

        # go up
        while is_inbound(x, y - 1, size) and matrix[y - 1][x] == 0:
            y = y - 1
            matrix[y][x] = next(sequence_generator)

    return matrix


def has_zero(matrix: [[int]]):
    return any([0 in row for row in matrix])


def is_inbound(x: int, y: int, size):
    return 0 <= x < size and 0 <= y < size


def number_sequence(start, end, step=1):
    current = start
    while current <= end:
        yield current
        current += step
