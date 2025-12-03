import math
from turtledemo.sorting_animate import instructions1


def puzzle_1(instructions: [int]) -> int:
    position = 50
    zero_hit = 0
    for instruction in instructions:
        direction = instruction[0]
        offset = int(instruction[1:])
        if direction == 'R':
            position = position + offset
            position = position % 100
        if direction == 'L':
            position = position - offset
            position = position % 100
        if position == 0:
            zero_hit = zero_hit + 1

    return zero_hit

def puzzle_2(instructions: [str]) -> int:
    position = 50
    zero_hit = 0
    for instruction in instructions:
        direction = instruction[0]
        offset = int(instruction[1:])

        if direction == 'R':
            new_position = position + offset
            zero_hit = zero_hit + rotate_and_count_zeros(position, 1, new_position)
            position = new_position
        elif direction == 'L':
            new_position = position - offset
            zero_hit = zero_hit + rotate_and_count_zeros(position, -1, new_position)
            position = new_position
        else:
            raise ValueError(f'Invalid direction: {direction}')

    return zero_hit

def rotate_and_count_zeros(start: int, direction: int, destination: int) -> int:
    zero_hit = 0
    current_position = start

    while current_position != destination:
        current_position = current_position + direction
        if current_position % 100 == 0:
            zero_hit = zero_hit + 1

    return zero_hit;