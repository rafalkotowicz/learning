import string


# PART 1
def get_priority(letter: str) -> int:
    return string.ascii_letters.find(letter) + 1


def get_common_in_line(rucksack: str) -> str:
    left = rucksack[:len(rucksack) // 2]
    right = rucksack[len(rucksack) // 2:]
    return set(left).intersection(set(right)).pop()


with open('../test/resources/day03.txt') as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        sum += get_priority(get_common_in_line(line))

print(sum)

assert get_priority('p') == 16
assert get_priority('L') == 38
assert get_priority('P') == 42
assert get_priority('v') == 22
assert get_priority('t') == 20
assert get_priority('s') == 19
assert get_common_in_line('vJrwpWtwJgWrhcsFMMfFFhFp') == 'p'


# PART 2

def get_common_in_lines(lines: str) -> str:
    common: set(str) = set(lines[0])
    for line in lines:
        common = common.intersection(set(line))
    common.remove('\n')
    return common.pop()


with open('../test/resources/day03.txt') as f:
    lines = f.readlines()
    sum = 0
    need_3: [str] = []
    for line in lines:
        need_3.append(line)
        if len(need_3) == 3:
            sum += get_priority(get_common_in_lines(need_3))
            need_3.clear()

print(sum)

assert get_common_in_lines(['vJrwpWtwJgWrhcsFMMfFFhFp\n','jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n','PmmdzqPrVvPwwTWBwg\n']) == 'r'
assert get_common_in_lines(['wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n','ttgJtRGJQctTZtZT\n','CrZsJsPPZsGzwwsLwLmpwMDw\n']) == 'Z'
