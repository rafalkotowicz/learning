from collections import deque

noof_books = int(input().strip())

books_stack = deque()
for _i in range(0, noof_books):
    command = input().strip()
    if command.startswith("BUY"):
        books_stack.append(command.replace("BUY ", ""))
    if command == "READ":
        print(books_stack.pop())
