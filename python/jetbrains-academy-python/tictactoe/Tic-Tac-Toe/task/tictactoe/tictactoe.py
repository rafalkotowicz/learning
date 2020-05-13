import sys

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
        if(curr_col == 0):
            print("|",end="")
            print(" ", end="")
        print(board[curr_row][curr_col], end="")
        print(" ", end="")
        if(curr_col == max_cols - 1):
            print("|",end="")
        curr_col += 1
    print()
    curr_row += 1
    curr_col = 0
print("---------")

# win condition detection - row
x, o = 0, 0
for row in range(max_rows):
    for col in range(max_cols):
        if board[row][col] == "X":
            x += 1
        elif board[row][col] == "O":
            o += 1
    if x == 3:
        print("X wins")
        sys.exit()
    if o == 3:
        print("O wins")
        sys.exit()
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
        print("X wins")
        sys.exit()
    if o == 3:
        print("O wins")
        sys.exit()
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
        print("X wins")
        sys.exit()
    if o == 3:
        print("O wins")
        sys.exit()

# win condition detection - diagonal /
# [0, 2]
# [1, 1]
# [2, 0]
