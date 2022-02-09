import math


def score(x, y):
    radius = math.sqrt(x ** 2 + y ** 2)
    if radius <= 1:
        points = 10
    elif radius <= 5:
        points = 5
    elif radius <= 10:
        points = 1
    else:
        points = 0
    return points
