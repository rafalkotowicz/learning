"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""
FACE_CARDS = ['J', 'Q', 'K']
CARDS_10 = FACE_CARDS + ['10']
CARDS_10_SCORE = 10


def value_of_card(card: str) -> int:
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    """

    if card in FACE_CARDS:
        return CARDS_10_SCORE
    elif card == 'A':
        return 1
    else:
        return int(card)


def higher_card(card_one: str, card_two: str):
    """Determine which card has a higher value in the hand.

    :param card_one: str - card dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    :param card_two: str - card dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    :return: higher value card - str. Tuple of both cards if they are of equal value.
    """

    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)

    if card_one_value > card_two_value:
        return card_one
    elif card_two_value > card_one_value:
        return card_two
    else:
        return card_one, card_two


def value_of_ace(card_one: str, card_two: str) -> int:
    """Calculate the most advantageous value for the ace card.

    :param card_one: str - card dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    :param card_two: str - card dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    :return: int - value of the upcoming ace card (either 1 or 11).
    """

    card_one_value = 11 if card_one == 'A' else value_of_card(card_one)
    card_two_value = 11 if card_two == 'A' else value_of_card(card_two)
    hand_score = card_one_value + card_two_value
    if hand_score <= 10:
        return 11
    else:
        return 1


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one: str - card dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    :param card_two: str - card dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    :return: bool - if the hand is a blackjack (two cards worth 21).
    """

    return (card_one == 'A' or card_two == 'A') and (card_one in CARDS_10 or card_two in CARDS_10)


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Determine if a player can split their hand into two hands.

    :param card_one: str - card dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    :param card_two: str - card dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).
    """

    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one: str, card_two: str) -> bool:
    """Determine if a blackjack player can place a double down bet.

    :param card_one: str - card dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    :param card_two: str - card dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """

    return True if value_of_card(card_one) + value_of_card(card_two) in range(9, 12) else False
