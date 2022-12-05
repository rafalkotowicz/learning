# PART 1
# [B]                     [N]     [H]
# [V]         [P] [T]     [V]     [P]
# [W]     [C] [T] [S]     [H]     [N]
# [T]     [J] [Z] [M] [N] [F]     [L]
# [Q]     [W] [N] [J] [T] [Q] [R] [B]
# [N] [B] [Q] [R] [V] [F] [D] [F] [M]
# [H] [W] [S] [J] [P] [W] [L] [P] [S]
# [D] [D] [T] [F] [G] [B] [B] [H] [Z]
#  1   2   3   4   5   6   7   8   9
import re

with open('day05.txt') as f:
    lines = f.readlines()


def print_hanoi() -> None:
    [print(f'#{id + 1} {tower}') for id, tower in enumerate(hanoi)]


def extract_values(line: str) -> [int]:
    line = re.sub('move |from | to', '', line)
    numbers = line.split()
    return [int(num) for num in numbers]


hanoi = [
    ['D', 'H', 'N', 'Q', 'T', 'W', 'V', 'B'],
    ['D', 'W', 'B'],
    ['T', 'S', 'Q', 'W', 'J', 'C'],
    ['F', 'J', 'R', 'N', 'Z', 'T', 'P'],
    ['G', 'P', 'V', 'J', 'M', 'S', 'T'],
    ['B', 'W', 'F', 'T', 'N'],
    ['B', 'L', 'D', 'Q', 'F', 'H', 'V', 'N'],
    ['H', 'P', 'F', 'R'],
    ['H', 'P', 'N', 'L', 'B', 'M', 'S', 'Z']
    # I wrongly hardcoded above line, but still got valid result xD
    # I was debugging Part 2 way too long because of this.
    # I learned valuable lesson today ;)
]

def make_move(instructions: [int]) -> None:
    quantity, _from, to = instructions
    _from -= 1
    to -= 1

    for q in range(quantity):
        hanoi[to].append(hanoi[_from].pop())


def lets_go() -> None:
    for line in lines:
        make_move(extract_values(line))


assert extract_values('move 2 from 8 to 1') == [2, 8, 1]
lets_go()
print("".join([x[-1] for x in hanoi]))


# PART 2
hanoi = [
    ['D', 'H', 'N', 'Q', 'T', 'W', 'V', 'B'],
    ['D', 'W', 'B'],
    ['T', 'S', 'Q', 'W', 'J', 'C'],
    ['F', 'J', 'R', 'N', 'Z', 'T', 'P'],
    ['G', 'P', 'V', 'J', 'M', 'S', 'T'],
    ['B', 'W', 'F', 'T', 'N'],
    ['B', 'L', 'D', 'Q', 'F', 'H', 'V', 'N'],
    ['H', 'P', 'F', 'R'],
    ['Z', 'S', 'M', 'B', 'L', 'N', 'P', 'H']
]


def make_move_9001(instructions: [int]) -> None:
    quantity, _from, to = instructions
    _from -= 1
    to -= 1

    hanoi[to].extend(hanoi[_from][-quantity:])
    for q in range(quantity):
        hanoi[_from].pop()


def lets_go_9001() -> None:
    for id, line in enumerate(lines):
        make_move_9001(extract_values(line))


lets_go_9001()
print("".join([x[-1] for x in hanoi]))
# assert 'BNTHFPNMW' == 'BNTHFPNMW' == 'BNTHFPNMW' == 'BNTHFPNMW' == 'BNTZFPMMW'
