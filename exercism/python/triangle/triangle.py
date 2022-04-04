def is_triangle(sides):
    return sides[0] + sides[1] > sides[2] and sides[1] + sides[2] > sides[0] and sides[2] + sides[0] > sides[1]


def all_sides_exists(sides):
    return sides[0] != 0 and sides[1] != 0 and sides[2] != 0


def equilateral(sides):
    return sides[0] == sides[1] == sides[2] and all_sides_exists(sides)


def isosceles(sides):
    are_two_sides_equal = False

    if sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]:
        are_two_sides_equal = True

    return is_triangle(sides) and are_two_sides_equal and all_sides_exists(sides)


def scalene(sides):
    return not isosceles(sides) and is_triangle(sides)
