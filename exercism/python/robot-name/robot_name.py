import random
import string
from uuid import uuid4


def name_generator():
    random.seed(str(uuid4()))
    random_string = random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
    random_number = random.randint(100, 999)
    return random_string.upper() + str(random_number)


class Robot:
    def __init__(self):
        self.name = name_generator()

    def reset(self):
        self.name = name_generator()
