# Score categories.
# Change the values as you see fit.
YACHT = (lambda x: 50 if len(set(x)) == 1 else 0)
ONES = (lambda x: sum_of_digits(x,1))
TWOS = (lambda x: sum_of_digits(x,2))
THREES = (lambda x: sum_of_digits(x,3))
FOURS = (lambda x: sum_of_digits(x,4))
FIVES = (lambda x: sum_of_digits(x,5))
SIXES = (lambda x: sum_of_digits(x,6))
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = sum

def sum_of_digits(x: list[int], digit):
    return x.count(digit) * digit

def score(dices: list[int], category) -> int:
    if category == "FULL_HOUSE":
        dices.sort()
        if dices[0] == dices[1] and dices[3] == dices[4] \
                and (dices[2] == dices[1] or dices[2] == dices[3]) \
                and dices[0] != dices[4]:
            return sum(dices)
        else:
            return 0
    elif category == "FOUR_OF_A_KIND":
        dices.sort()
        rolls: dict = dict()
        for dice in dices:
            if dice in rolls:
                rolls[dice] += 1
            else:
                rolls[dice] = 1
        for roll in rolls:
            if rolls[roll] >= 4:
                return 4 * roll
        return 0;
    elif category == "LITTLE_STRAIGHT":
        dices.sort()
        if dices[0] == 1 and dices[1] == 2 and dices[2] == 3 and dices[3] == 4 and dices[4] == 5:
            return 30
        return 0
    elif category == "BIG_STRAIGHT":
        dices.sort()
        if dices[0] == 2 and dices[1] == 3 and dices[2] == 4 and dices[3] == 5 and dices[4] == 6:
            return 30
        return 0

    return category(dices)
