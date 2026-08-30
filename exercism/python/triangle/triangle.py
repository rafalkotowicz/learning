"""Triangle classification helpers for the Exercism triangle exercise."""

ISOSCELES_MAX_UNIQUE_SIDES = 2
SCALENE_UNIQUE_SIDES = 3


def is_triangle(sides) -> bool:
    """Return True when provided sides can form a non-degenerate triangle."""
    if not all_sides_exists(sides):
        return False

    first_side, second_side, third_side = sides
    return (
        first_side + second_side > third_side
        and second_side + third_side > first_side
        and first_side + third_side > second_side
    )


def all_sides_exists(sides) -> bool:
    """Return True when all sides have a positive, non-zero length."""
    return all(side_length > 0 for side_length in sides)


def equilateral(sides) -> bool:
    """Return True when all sides are equal and the sides form a triangle."""
    return is_triangle(sides) and len(set(sides)) == 1


def isosceles(sides) -> bool:
    """Return True when at least two sides are equal and valid triangle rules pass."""
    return is_triangle(sides) and len(set(sides)) <= ISOSCELES_MAX_UNIQUE_SIDES


def scalene(sides) -> bool:
    """Return True when all sides are different and the sides form a triangle."""
    return is_triangle(sides) and len(set(sides)) == SCALENE_UNIQUE_SIDES
