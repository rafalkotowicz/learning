# Score categories.
# Change the values as you see fit.
YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"


def score(dices: list[int], category) -> int:
    def filtered_sum(i):
        return sum(filter(lambda x: x == i, dices))

    # Python 3.10
    # match category:
    #     case "YACHT":
    #         if dices[0] == dices[1] and dices[1] == dices[2] \
    #                 and dices[2] == dices[3] and dices[3] == dices[4]:
    #             return 50
    #         else:
    #             return 0
    #     case "ONES":
    #         return filtered_sum(1)
    #     case "TWOS":
    #         return filtered_sum(2)
    #     case "THREES":
    #         return filtered_sum(3)
    #     case "FOURS":
    #         return filtered_sum(4)
    #     case "FIVES":
    #         return filtered_sum(5)
    #     case "SIXES":
    #         return filtered_sum(6)
    #     case "FULL_HOUSE":
    #         dices.sort()
    #         if dices[0] == dices[1] and dices[3] == dices[4] \
    #                 and (dices[2] == dices[1] or dices[2] == dices[3]) \
    #                 and dices[0] != dices[4]:
    #             return sum(dices)
    #         else:
    #             return 0
    #     case "FOUR_OF_A_KIND":
    #         dices.sort()
    #         rolls: dict = dict()
    #         for dice in dices:
    #             if dice in rolls:
    #                 rolls[dice] += 1
    #             else:
    #                 rolls[dice] = 1
    #         for roll in rolls:
    #             if rolls[roll] >= 4:
    #                 return 4 * roll
    #         return 0;
    #     case "LITTLE_STRAIGHT":
    #         dices.sort()
    #         if dices[0] == 1 and dices[1] == 2 and dices[2] == 3 and dices[3] == 4 and dices[4] == 5:
    #             return 30
    #         return 0
    #     case "BIG_STRAIGHT":
    #         dices.sort()
    #         if dices[0] == 2 and dices[1] == 3 and dices[2] == 4 and dices[3] == 5 and dices[4] == 6:
    #             return 30
    #         return 0
    #     case "CHOICE":
    #         return sum(dices)
    #     case _:
    #         return 0

    # Python 3.9
    if category == "YACHT":
        if dices[0] == dices[1] and dices[1] == dices[2] \
                and dices[2] == dices[3] and dices[3] == dices[4]:
            return 50
        else:
            return 0
    elif category == "ONES":
        return filtered_sum(1)
    elif category == "TWOS":
        return filtered_sum(2)
    elif category == "THREES":
        return filtered_sum(3)
    elif category == "FOURS":
        return filtered_sum(4)
    elif category == "FIVES":
        return filtered_sum(5)
    elif category == "SIXES":
        return filtered_sum(6)
    elif category == "FULL_HOUSE":
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
    elif category == "CHOICE":
        return sum(dices)
