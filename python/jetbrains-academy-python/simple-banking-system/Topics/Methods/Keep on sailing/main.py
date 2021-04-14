class Ship:
    def __init__(self, name):
        self.name = name

    def sail(self, destination):
        return f"The {self.name} has sailed for {destination}!"


black_pearl = Ship("Black Pearl")
print(black_pearl.sail(input()))
