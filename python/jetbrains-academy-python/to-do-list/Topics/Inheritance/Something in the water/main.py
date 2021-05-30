class WaterBody:
    def __init__(self, name, length):
        self.name = name  # str
        self.length = length  # int


class River(WaterBody):
    def __init__(self, name, length):
        super().__init__(name, length)


seine = River("Seine", 777)
