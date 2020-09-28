from collections import deque

no_of_items = int(input().strip())

my_stack = deque()
for _i in range(0, no_of_items):
    operation = input().split()
    if operation[0] == "PUSH":
        my_stack.append(operation[1])
    if operation[0] == "POP":
        my_stack.pop()

for _i in range(0, len(my_stack)):
    print(my_stack.pop())
