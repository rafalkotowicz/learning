state = [['X', 'O', 'X'],
         ['O', 'X', 'O'],
         ['X', 'X', 'O']]

max_rows = 3
curr_row = 0
max_cols = 3
curr_col = 0
while curr_row < max_rows:
    while curr_col < max_cols:
        print(state[curr_row][curr_col], end="")
        print(" ", end="")
        curr_col += 1
    print()
    curr_row += 1
    curr_col = 0
