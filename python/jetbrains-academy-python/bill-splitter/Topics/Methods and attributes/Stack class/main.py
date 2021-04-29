class Stack:

    def __init__(self):
        self.my_stack = list()

    def push(self, el):
        self.my_stack.append(el)

    def pop(self):
        return self.my_stack.pop()

    def peek(self):
        last_item = self.my_stack.pop()
        self.my_stack.append(last_item)
        return last_item

    def is_empty(self):
        return bool(len(self.my_stack) == 0)
