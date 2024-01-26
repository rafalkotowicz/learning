def is_matrix_regular(matrix):
    if len(set([len(row) for row in matrix])) != 1:
        raise ValueError('irregular matrix')


def is_highest_in_row(matrix, row_index, tree_height):
    return max(matrix[row_index]) <= tree_height


def is_smallest_in_column(matrix, column_index, tree_height):
    return tree_height <= min(matrix[row_2][column_index] for row_2 in range(0, len(matrix)))


def saddle_points(matrix: [[str]]):
    if len(matrix) == 0:
        return []
    is_matrix_regular(matrix)

    fount_points = []

    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[0])):
            tree_height = matrix[row][col]
            if is_highest_in_row(matrix, row, tree_height) and is_smallest_in_column(matrix, col, tree_height):
                fount_points.append({'row': row + 1, 'column': col + 1})
    return fount_points
