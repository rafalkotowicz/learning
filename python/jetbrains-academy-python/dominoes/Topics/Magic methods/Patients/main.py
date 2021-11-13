class Patient:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.last_name}. {self.age}"

    def __repr__(self):
        return f"Object of the class {self.__class__.__name__}. name: {self.name}, " \
               f"last_name: {self.last_name}, age: {self.age}"

# "TESTS"
# john = Patient("John", "Doe", 50)
# print(john)
# print(repr(john))
