user_input = input()

state = [[user_input[0], user_input[1], user_input[2]],
         [user_input[3], user_input[4], user_input[5]],
         [user_input[6], user_input[7], user_input[8]]]

# state = [['X', 'O', 'X'],
#          ['O', 'X', 'O'],
#          ['X', 'X', 'O']]

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
        print(state[curr_row][curr_col], end="")
        print(" ", end="")
        if(curr_col == max_cols - 1):
            print("|",end="")
        curr_col += 1
    print()
    curr_row += 1
    curr_col = 0
print("---------")