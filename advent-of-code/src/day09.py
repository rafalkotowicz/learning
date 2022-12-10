import math

from utils.common import read_and_sanitize

lines = read_and_sanitize('../test/resources/day09.txt')

SIZE = 500
SIZE_W = SIZE
SIZE_H = SIZE
# SIZE_W = 6
# SIZE_H = 5
bridge: [[str]] = [['.'] * SIZE_W for i in range(SIZE_H)]
START: (int, int) = (4, 0)
# START: (int, int) = (SIZE // 2, SIZE // 2)
TAIL_POS_LOG: [(int, int)] = []


# PART 1, 5873 + 1 :)
def print_current_state():
    for row in range(SIZE_H):
        for col in range(SIZE_W):
            print(bridge[row][col], end='')
        print()


def mark_new_positions(head, tails):
    for row in range(SIZE_H):
        for col in range(SIZE_W):
            bridge[row][col] = '.'

    bridge[START[0]][START[1]] = 's'
    for i in range(len(tails) - 1, -1, -1):
        bridge[tails[i][0]][tails[i][1]] = i + 1
    bridge[head[0]][head[1]] = 'H'


def move_head_by_1(head, change) -> (int, int):
    return head[0] + change[0], head[1] + change[1]


def is_tail_moving(head, tail) -> bool:
    return math.fabs(head[0] - tail[0]) > 1 or math.fabs(head[1] - tail[1]) > 1


def move_tail_by_1(head, tail):
    h_y, h_x = head
    t_y, t_x = tail
    dy = t_y - h_y
    dx = t_x - h_x

    if dy == -2 and math.fabs(dx) <= 1:
        tail = h_y - 1, h_x
    elif math.fabs(dy) <= 1 and dx == 2:
        tail = h_y, h_x + 1
    elif dy == 2 and math.fabs(dx) <= 1:
        tail = h_y + 1, h_x
    elif math.fabs(dy) <= 1 and dx == -2:
        tail = h_y, h_x - 1
    elif dy == -2 and dx == 2:
        tail = h_y - 1, h_x + 1
    elif dy == 2 and dx == 2:
        tail = h_y + 1, h_x + 1
    elif dy == 2 and dx == -2:
        tail = h_y + 1, h_x - 1
    elif dy == -2 and dx == -2:
        tail = h_y - 1, h_x - 1

    return tail


def make_move(head, tails: [(int, int)], direction, distance):
    change: (int, int) = (0, 0)
    if direction == 'U':
        change = (-1, 0)
    elif direction == 'R':
        change = (0, 1)
    elif direction == 'D':
        change = (1, 0)
    elif direction == 'L':
        change = (0, -1)
    else:
        raise ValueError(f'Cannot parse direction: {direction}')

    for i in range(distance):
        head = move_head_by_1(head, change)
        tmp_head = head
        for j in range(len(tails)):
            if is_tail_moving(tmp_head, tails[j]):
                tails[j] = move_tail_by_1(tmp_head, tails[j])
                if j == 8:
                    TAIL_POS_LOG.append(tails[j])
            else:
                break
            tmp_head = tails[j]
        mark_new_positions(head, tails)
        # print_current_state()

    return head, tails


def process_input(lines) -> bridge:
    head = START
    tails = [START for i in range(0, 9)]
    mark_new_positions(head, tails)
    # print_current_state()

    for id, line in enumerate(lines):
        print(f'== {id}. {line} ==')
        direction, distance = line.split()
        distance = int(distance)
        head, tails = make_move(head, tails, direction, distance)
        # print_current_state()
    return bridge


process_input(lines)
print(len(set(TAIL_POS_LOG)) + 1)

# Part 2, 2467
