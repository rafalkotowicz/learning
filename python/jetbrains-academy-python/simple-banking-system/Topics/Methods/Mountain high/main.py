class Mountain:
    meters_in_feet = 0.3048

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def convert_height(self):
        return self.height / Mountain.meters_in_feet
