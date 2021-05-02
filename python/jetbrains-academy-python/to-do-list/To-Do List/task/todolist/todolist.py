class Todo:
    todos = []

    def __init__(self, title):
        self.title = title
        Todo.todos.append(self)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Todo({self.title})"


todo1 = Todo("1) Do yoga")
todo2 = Todo("2) Make breakfast")
todo3 = Todo("3) Learn basics of SQL")
todo4 = Todo("4) Learn what is ORM")

print("Today:")
for todo in Todo.todos:
    print(todo)
