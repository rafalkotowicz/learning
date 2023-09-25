def rows(row_count: int) -> [int]:
    if row_count < 0:
        raise ValueError("number of rows is negative")
    elif row_count == 0:
        return []
    elif row_count == 1:
        return [[1]]
    else:
        previous_triangle = rows(row_count - 1)
        last_row = previous_triangle[-1]
        new_row = [1]
        for i in range(1, len(last_row)):
            new_row.append(last_row[i - 1] + last_row[i])
        new_row.append(1)
        previous_triangle.append(new_row)
        return previous_triangle
