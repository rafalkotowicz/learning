ROCK = ['A', 'X']
PAPER = ['B', 'Y']
SCISSORS = ['C', 'Z']

shape_score = {
    'A': 1,
    'X': 1,
    'B': 2,
    'Y': 2,
    'C': 3,
    'Z': 3
}

def match_points(match: [str]) -> int:
    other, me = match
    if me == 'X':
        if other in ROCK:
            me = 'C'
        elif other in PAPER:
            me = 'A'
        else:
            me = 'B'
    elif me == 'Y':
        me = other
    else:
        if other in ROCK:
            me = 'B'
        elif other in PAPER:
            me = 'C'
        else:
            me = 'A'


    if me in ROCK and other in ROCK or me in PAPER and other in PAPER or me in SCISSORS and other in SCISSORS:
        return 3 + shape_score[me]
    elif me in ROCK and other in SCISSORS or me in PAPER and other in ROCK or me in SCISSORS and other in PAPER:
        return 6 + shape_score[me]
    else:
        return 0 + shape_score[me]


with open('../test/resources/day02.txt') as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        sum += match_points(line.split())


print(sum)



# print(match_points(['A', 'Y']))
# print(match_points(['B', 'X']))
# print(match_points(['C', 'Z']))