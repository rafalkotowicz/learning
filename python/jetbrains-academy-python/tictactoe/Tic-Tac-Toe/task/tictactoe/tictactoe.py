user_input = input()
board = [[user_input[0], user_input[1], user_input[2]],
         [user_input[3], user_input[4], user_input[5]],
         [user_input[6], user_input[7], user_input[8]]]

print("---------")
max_rows = 3
curr_row = 0
max_cols = 3
curr_col = 0
while curr_row < max_rows:
    while curr_col < max_cols:
        if curr_col == 0:
            print("|", end="")
            print(" ", end="")
        print(board[curr_row][curr_col], end="")
        print(" ", end="")
        if curr_col == max_cols - 1:
            print("|", end="")
        curr_col += 1
    print()
    curr_row += 1
    curr_col = 0
print("---------")

who_won = []
# win condition detection - row
x, o = 0, 0
for row in range(max_rows):
    for col in range(max_cols):
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
for col in range(max_cols):
    for row in range(max_rows):
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
for col in range(max_cols):
    for row in range(max_rows):
        if row == col and board[row][col] == "X":
            x += 1
        elif row == col and board[row][col] == "O":
            o += 1
    if x == 3:
        who_won.append("X wins")
    if o == 3:
        who_won.append("O wins")

x_moves = len([x for row in range(max_rows) for col in range(max_cols) if board[row][col] == "X"])
o_moves = len([x for row in range(max_rows) for col in range(max_cols) if board[row][col] == "O"])
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
elif len(who_won) > 1 or abs(x_moves - o_moves) >= 2:
    print("Impossible")
elif len(who_won) == 0 and not game_finished:
    print("Game not finished")
elif len(who_won) == 1:
    print(who_won[0])
