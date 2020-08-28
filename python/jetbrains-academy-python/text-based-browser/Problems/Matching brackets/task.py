from collections import deque

my_stack = deque(list(input().strip()))

open_brackets = 0
is_valid = True
for _i in range(0, len(my_stack)):
    curr_char = my_stack.pop()
    if curr_char == ')':
        open_brackets += 1
    elif curr_char == '(':
        if open_brackets < 1:
            is_valid = False
        else:
            open_brackets -= 1

if open_brackets != 0:
    is_valid = False

print("OK" if is_valid else "ERROR")
