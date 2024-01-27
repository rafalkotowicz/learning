def validate_input_grid_height(input_grid: [str]) -> None:
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")


def validate_input_grid_width(input_grid: [str]) -> None:
    if any([len(row) % 3 != 0 for row in input_grid]):
        raise ValueError("Number of input columns is not a multiple of three")


def recognize_digit(matrix: [str]) -> str:
    zero = [" _ ",
            "| |",
            "|_|",
            "   "]
    one = ["   ",
           "  |",
           "  |",
           "   "]
    two = [" _ ",
           " _|",
           "|_ ",
           "   "]
    three = [" _ ",
             " _|",
             " _|",
             "   "]
    four = ["   ",
            "|_|",
            "  |",
            "   "]
    five = [" _ ",
            "|_ ",
            " _|",
            "   "]
    six = [" _ ",
           "|_ ",
           "|_|",
           "   "]
    seven = [" _ ",
             "  |",
             "  |",
             "   "]
    eight = [" _ ",
             "|_|",
             "|_|",
             "   "]
    nine = [" _ ",
            "|_|",
            " _|",
            "   "]

    if matrix == zero:
        return '0'
    elif matrix == one:
        return '1'
    elif matrix == two:
        return '2'
    elif matrix == three:
        return '3'
    elif matrix == four:
        return '4'
    elif matrix == five:
        return '5'
    elif matrix == six:
        return '6'
    elif matrix == seven:
        return '7'
    elif matrix == eight:
        return '8'
    elif matrix == nine:
        return '9'
    elif matrix == [',']:
        return ','
    else:
        return '?'


def convert(input_grid: [str]) -> "str":
    validate_input_grid_height(input_grid)
    validate_input_grid_width(input_grid)

    digits_separated = []
    for row in range(0, len(input_grid), 4):
        for col in range(0, len(input_grid[row]), 3):
            digit = []
            digit.append(input_grid[row][col: col + 3])
            digit.append(input_grid[row + 1][col: col + 3])
            digit.append(input_grid[row + 2][col: col + 3])
            digit.append(input_grid[row + 3][col: col + 3])
            digits_separated.append(digit)
        if row < len(input_grid) - 4:
            digits_separated.append([","])

    return ''.join([recognize_digit(x) for x in digits_separated])
