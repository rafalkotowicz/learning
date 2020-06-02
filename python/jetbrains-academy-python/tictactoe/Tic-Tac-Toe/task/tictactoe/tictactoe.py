import sys

initialize = "_________"
board = [[initialize[0], initialize[1], initialize[2]],
         [initialize[3], initialize[4], initialize[5]],
         [initialize[6], initialize[7], initialize[8]]]
MAX_COLS = 3
MAX_ROWS = 3


def print_board():
    print("---------")

    curr_row = 0

    curr_col = 0
    while curr_row < MAX_ROWS:
        while curr_col < MAX_COLS:
            if curr_col == 0:
                print("|", end="")
                print(" ", end="")
            if board[curr_row][curr_col] == "_":
                print(" ", end="")
            else:
                print(board[curr_row][curr_col], end="")
            print(" ", end="")
            if curr_col == MAX_COLS - 1:
                print("|", end="")
            curr_col += 1
        print()
        curr_row += 1
        curr_col = 0
    print("---------")


def state_check():
    who_won = []
    # win condition detection - row
    x, o = 0, 0
    for row in range(MAX_ROWS):
        for col in range(MAX_COLS):
            if board[row][col] == "X":
                x += 1
            elif board[row][col] == "O":
                o += 1
        if x == 3:
            who_won.append("X wins")
        if o == 3:
            who_won.append("O wins")
        x, o = 0, 0

    # win condition detection - column
    x, o = 0, 0
    for col in range(MAX_COLS):
        for row in range(MAX_ROWS):
            if board[row][col] == "X":
                x += 1
            elif board[row][col] == "O":
                o += 1
        if x == 3:
            who_won.append("X wins")
        if o == 3:
            who_won.append("O wins")
        x, o = 0, 0

    # win condition detection - diagonal \
    x, o = 0, 0
    for col in range(MAX_COLS):
        for row in range(MAX_ROWS):
            if row == col and board[row][col] == "X":
                x += 1
            elif row == col and board[row][col] == "O":
                o += 1
        if x == 3:
            who_won.append("X wins")
        if o == 3:
            who_won.append("O wins")

    x_moves = len([x for row in range(MAX_ROWS) for col in range(MAX_COLS) if board[row][col] == "X"])
    o_moves = len([x for row in range(MAX_ROWS) for col in range(MAX_COLS) if board[row][col] == "O"])
    game_finished = (x_moves + o_moves) == 9
    # win condition detection - diagonal /
    # [0, 2]
    # [1, 1]
    # [2, 0]
    if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        who_won.append("X wins")
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        who_won.append("O wins")

    if len(who_won) == 0 and game_finished:
        print("Draw")
    # elif len(who_won) > 1 or abs(x_moves - o_moves) >= 2:
    #     print("Impossible")
    # elif len(who_won) == 0 and not game_finished:
    #     print("Game not finished")
    elif len(who_won) == 1:
        print(who_won[0])
        game_finished = True

    return game_finished


valid_range = [1, 2, 3]


def validate_input(col, row):
    if not str(col).isdigit() or not str(row).isdigit():
        print("You should enter numbers!")
        return False
    col = int(col)
    row = int(row)
    if col not in valid_range or row not in valid_range:
        print("Coordinates should be from 1 to 3!")
        return False
    elif read_cell(col, row) != "_":
        print("This cell is occupied! Choose another one!")
        return False
    else:
        return True


def write_cell(col, row, val):
    board[3 - int(row)][int(col) - 1] = val


def read_cell(col, row):
    return board[3 - int(row)][int(col) - 1]


move = "X"

print_board()
col, row = input("Enter the coordinates: ").split()
while 1:
    if validate_input(col, row):
        write_cell(col, row, move)
        print_board()
        if state_check():
            sys.exit()
        if move == "X":
            move = "O"
        else:
            move = "X"
    else:
        col, row = input("Enter the coordinates: ").split()
