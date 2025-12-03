import math
from turtledemo.sorting_animate import instructions1


def puzzle_1(instructions):
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

def puzzle_1_1(instructions):
    position = 50
    zero_hit = 0

    for instruction in instructions:
        direction = instruction[0]
        offset = int(instruction[1:])

        if direction == 'R':
            position = position + offset
        elif direction == 'L':
            position = position - offset
        else:
            raise ValueError(f'Invalid direction: {direction}')

        if position == 0 or position == 100:
            zero_hit = zero_hit + 1
            position = 0
            continue

        while position < 0 or position > 100:
            if position > 100:
                # zero_hit = zero_hit + 1
                position = position - 100
            elif position < 0:
                # zero_hit = zero_hit + 1
                position = position + 100

    return zero_hit


def puzzle_2(instructions):
    position = 50
    zero_hit = 0
    for instruction in instructions:
        direction = instruction[0]
        offset = int(instruction[1:])

        if direction == 'R':
            position = position + offset
        elif direction == 'L':
            position = position - offset
        else:
            raise ValueError(f'Invalid direction: {direction}')

        while position < 0 or position > 100:
            if position >= 100:
                if position == 100:
                    zero_hit = zero_hit + 1
                    position = 0
                    break
                else:
                    zero_hit = zero_hit + 1
                    position = position - 100
            elif position < 0:
                zero_hit = zero_hit + 1
                position = position + 100

    return zero_hit