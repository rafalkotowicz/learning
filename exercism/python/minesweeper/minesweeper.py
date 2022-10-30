MINE = "*"


def validate_minefied_chars(minefield: [str]) -> bool:
    return all([all(c in "* " for c in row) for row in minefield])


def validate_minefied_dimensions(minefield: [str]) -> bool:
    return len(set(list(map(len, minefield)))) <= 1


def annotate(minefield: [str]) -> str:
    if len(minefield) == 0:
        return []
    max_row = len(minefield)
    max_column = len(minefield[0])

    if not validate_minefied_chars(minefield):
        raise ValueError("The board is invalid with current input.")
    if not validate_minefied_dimensions(minefield):
        raise ValueError("The board is invalid with current input.")

    result_minefield: [] = ["" for row in minefield]

    for row_id, row_value in enumerate(minefield):
        for col_id, col_value in enumerate(row_value):
            if minefield[row_id][col_id] == MINE:
                result_minefield[row_id] += MINE
            else:
                neighbours = [(row_id_2, col_id_2)
                              for row_id_2 in range(row_id - 1, row_id + 2)
                              for col_id_2 in range(col_id - 1, col_id + 2)
                              if (-1 < row_id < max_row and -1 < col_id < max_column and
                                  (row_id != row_id_2 or col_id != col_id_2) and
                                  (0 <= row_id_2 < max_row) and (0 <= col_id_2 < max_column))
                              ]
                surrounding_mines = sum([1 for n in neighbours if minefield[n[0]][n[1]] == "*"])
                result_minefield[row_id] += str(surrounding_mines) if surrounding_mines > 0 else " "

    return result_minefield
