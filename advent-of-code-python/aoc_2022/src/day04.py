# PART 1
def is_subset(ranges: ([int], [int])) -> bool:
    range_1, range_2 = ranges
    s1 = set(range_1)
    s2 = set(range_2)
    return s1.issubset(s2) or s2.issubset(s1)


def get_ranges(line: str) -> ([int], [int]):
    range_1_min = int(line.split(",")[0].split('-')[0])
    range_1_max = int(line.split(",")[0].split('-')[1])
    range_1 = [x for x in range(range_1_min, range_1_max + 1)]
    range_2_min = int(line.split(",")[1].split('-')[0])
    range_2_max = int(line.split(",")[1].split('-')[1])
    range_2 = [x for x in range(range_2_min, range_2_max + 1)]
    return range_1, range_2


def sanitize_line(line: str) -> str:
    return line.replace('\n', '')


with open('../test/resources/day04.txt') as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        line = sanitize_line(line)
        if is_subset(get_ranges(line)):
            sum += 1

print(sum)


# PART 2
def does_overlap(ranges: ([int], [int])) -> bool:
    range_1, range_2 = ranges
    s1 = set(range_1)
    s2 = set(range_2)
    return len(s1.intersection(s2)) != 0


with open('../test/resources/day04.txt') as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        line = sanitize_line(line)
        if does_overlap(get_ranges(line)):
            sum += 1

print(sum)