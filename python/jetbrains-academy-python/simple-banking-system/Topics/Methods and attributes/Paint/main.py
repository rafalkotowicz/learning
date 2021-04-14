class House:
    def __init__(self, floors):
        self.floors = floors
        self.color = None

    def paint(self, new_color):
        self.color = new_color
