import math
from random import randint


class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    @staticmethod
    def ability() -> int:
        result: list(int) = [randint(1, 6) for x in range(4)]
        result.sort()
        return sum(result[1::])


def modifier(value: int) -> int:
    return math.floor((value - 10) / 2)
