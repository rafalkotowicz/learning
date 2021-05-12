suit_rank = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace": 14,
}

rank_sum = 0
no_cards = 6
for i in range(0, no_cards):
    rank_sum += suit_rank.get(input())

print(rank_sum / no_cards)
