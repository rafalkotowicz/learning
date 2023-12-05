import re


def parse_one_line(line: str, winning_length: int) -> (int, [int], [int]):
    numbers = [int(x) for x in (re.findall(r'(\d+)', line))]
    return (numbers[0], numbers[1:(winning_length + 1)], numbers[(winning_length + 1):])


def find_hits(winning: [int], guesses: [int]) -> [int]:
    return [guess for guess in guesses if guess in winning]


def scratchard_worth(lines: str, winning_length) -> int:
    points = 0
    for line in lines:
        _, winnings, guesses = parse_one_line(line, winning_length)
        hits = len(find_hits(winnings, guesses))
        if hits > 0:
            points += 2 ** (hits - 1)

    return points


class Card:
    id: int
    winning: [int]
    guessing: [int]
    copies: int
    hits: int

    def __init__(self, id, winning, guesses):
        self.id = id
        self.winning = winning
        self.guessing = guesses
        self.copies = 1
        self.hits = len(find_hits(winning, guesses))

    def __repr__(self):
        return f'Card {self.id}: hits={self.hits}, copies={self.copies}'


def read_cards(lines: str, winning_length) -> [Card]:
    cards: [Card] = []
    for line in lines:
        card_id, winning, guesses = parse_one_line(line, winning_length)
        cards.append(Card(id, winning, guesses))
    return cards


def scratchards_won(lines: str, winning_length) -> int:
    cards: [Card] = read_cards(lines, winning_length)

    for id, card in enumerate(cards):
        for copy in range(card.copies):
            for hit in range(card.hits):
                cards[id + 1 + hit].copies += 1

    return sum(card.copies for card in cards)
