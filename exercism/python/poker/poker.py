class Card:
    value: str
    suit: str

    card_ranks: dict() = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "10": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
    }

    def __init__(self, card):
        if card[1] == "0":
            self.value = "10"
        else:
            self.value = card[0]
        self.suit = card[-1]

    def __eq__(self, other) -> bool:
        return self.value == other.value and self.suit == other.suit


class Hand:
    original_input: str = None
    cards: [Card] = None
    hand_rank: int = -1
    is_straight_flush: bool = False
    is_flush: bool = False
    is_straight: bool = False
    is_four_of_a_kind: bool = False
    is_full_house: bool = False
    is_three_of_a_kind: bool = False
    is_two_pair: bool = False
    is_one_pair: bool = False
    is_high_card: bool = False

    def __init__(self, cards: str):
        self.original_input = cards
        self.cards = [Card(card) for card in cards.split(" ")]
        if self._is_straight_flush():
            self.is_straight_flush = True
            self.hand_rank = 10
            return
        elif self._is_four_of_a_kind():
            self.is_four_of_a_kind = True
            self.hand_rank = 9
            return
        elif self._is_full_house():
            self.is_full_house = True
            self.hand_rank = 8
            return
        elif self._is_flush():
            self.is_flush = True
            self.hand_rank = 7
            return
        elif self._is_straight():
            self.is_straight = True
            self.hand_rank = 6
            return
        elif self._is_three_of_a_kind():
            self.is_three_of_a_kind = True
            self.hand_rank = 5
            return
        elif self._is_two_pair():
            self.is_two_pair = True
            self.hand_rank = 4
            return
        elif self._is_one_pair():
            self.is_one_pair = True
            self.hand_rank = 3
            return
        elif self._is_high_card():
            self.is_high_card = True
            self.hand_rank = 2

    def _is_flush(self) -> bool:
        return 1 == len(set([card.suit for card in self.cards]))

    def _is_straight(self) -> bool:
        is_straight: bool = False
        if self._has_given_card_rank("A"):
            ace_high: [int] = sorted([Card.card_ranks[card.value] for card in self.cards])
            ace_low: [int] = sorted([Card.card_ranks[card.value] if card.value != "A" else 1 for card in self.cards])
            is_straight = list(range(min(ace_high), max(ace_high) + 1)) == ace_high or list(
                range(min(ace_low), max(ace_low) + 1)) == ace_low
        else:
            aceless_hand: [int] = sorted([Card.card_ranks[card.value] for card in self.cards])
            is_straight = list(range(min(aceless_hand), max(aceless_hand) + 1)) == aceless_hand
        return is_straight

    def _has_given_card_rank(self, searched_card: str) -> bool:
        return len([card for card in self.cards if card.value == searched_card]) > 0

    def _group_cards(self):
        groups = dict()
        for card in self.cards:
            if card.value in groups.keys():
                groups[card.value] = groups[card.value] + 1
            else:
                groups[card.value] = 1
        return groups

    def _is_four_of_a_kind(self) -> bool:
        return [1, 4] == sorted(self._group_cards().values())

    def _is_full_house(self) -> bool:
        grouped: [int] = self._group_cards().values()
        return [2, 3] == sorted(grouped)

    def _is_three_of_a_kind(self) -> bool:
        grouped: [int] = self._group_cards().values()
        return [1, 1, 3] == sorted(grouped)

    def _is_two_pair(self) -> bool:
        grouped: [int] = self._group_cards().values()
        return [1, 2, 2] == sorted(grouped)

    def _is_one_pair(self) -> bool:
        grouped: [int] = self._group_cards().values()
        return [1, 1, 1, 2] == sorted(grouped)

    def _is_high_card(self) -> bool:
        grouped: [int] = self._group_cards().values()
        return [1, 1, 1, 1, 1] == sorted(grouped)

    def _is_straight_flush(self) -> bool:
        return self._is_straight() and self._is_flush()

    def _get_pair_values(self) -> [int]:
        pair_values: [str] = [card[0] for card in self._group_cards().items() if card[1] == 2]
        return sorted(self._value_to_ranks(pair_values), reverse=True)

    def _get_set_value(self) -> int:
        set_values: [str] = [card[0] for card in self._group_cards().items() if card[1] == 3]
        return self._value_to_ranks(set_values)[0]

    def _get_quads_value(self) -> int:
        set_values: [str] = [card[0] for card in self._group_cards().items() if card[1] == 4]
        return self._value_to_ranks(set_values)[0]

    def _get_cards_without_set(self) -> [int]:
        cards_without_set: [str] = [card[0] for card in self._group_cards().items() if card[1] == 1]
        return sorted(self._value_to_ranks(cards_without_set), reverse=True)

    def _value_to_ranks(self, values) -> [int]:
        return [Card.card_ranks[value] for value in values]

    def _compare_not_set_cards(self, other_hand):
        this_remaining = self._get_cards_without_set()
        other_remaining = other_hand._get_cards_without_set()
        for this, other in zip(this_remaining, other_remaining):
            if this > other:
                return self
            elif this < other:
                return other_hand
        return None

    def better_hand(self, other_hand):
        if self.hand_rank > other_hand.hand_rank:
            return self
        elif self.hand_rank < other_hand.hand_rank:
            return other_hand
        else:
            if self.is_high_card and other_hand.is_high_card:
                return self._compare_not_set_cards(other_hand)

            elif self.is_one_pair and other_hand.is_one_pair:
                if self._get_pair_values()[0] > other_hand._get_pair_values()[0]:
                    return self
                elif self._get_pair_values()[0] < other_hand._get_pair_values()[0]:
                    return other_hand
                else:
                    return self._compare_not_set_cards(other_hand)

            elif self.is_two_pair and other_hand.is_two_pair:
                if self._get_pair_values()[0] > other_hand._get_pair_values()[0]:
                    return self
                elif self._get_pair_values()[0] < other_hand._get_pair_values()[0]:
                    return other_hand
                else:
                    if self._get_pair_values()[1] > other_hand._get_pair_values()[1]:
                        return self
                    elif self._get_pair_values()[1] < other_hand._get_pair_values()[1]:
                        return other_hand
                    else:
                        return self._compare_not_set_cards(other_hand)

            elif self.is_three_of_a_kind and other_hand.is_three_of_a_kind:
                if self._get_set_value() > other_hand._get_set_value():
                    return self
                elif self._get_set_value() < other_hand._get_set_value():
                    return other_hand
                else:
                    return self._compare_not_set_cards(other_hand)

            elif self.is_full_house and other_hand.is_full_house:
                if self._get_set_value() > other_hand._get_set_value():
                    return self
                elif self._get_set_value() < other_hand._get_set_value():
                    return other_hand
                else:
                    if self._get_pair_values()[0] > other_hand._get_pair_values()[0]:
                        return self
                    elif self._get_pair_values()[0] < other_hand._get_pair_values()[0]:
                        return other_hand

            elif self.is_four_of_a_kind and other_hand.is_four_of_a_kind:
                if self._get_quads_value() > other_hand._get_quads_value():
                    return self
                elif self._get_quads_value() < other_hand._get_quads_value():
                    return other_hand
                else:
                    return self._compare_not_set_cards(other_hand)

            elif self.is_flush and other_hand.is_flush:
                return self._compare_not_set_cards(other_hand)

            elif self.is_straight and other_hand.is_straight:
                return self._compare_not_set_cards(other_hand)


def best_hands(hands: [str]) -> [str]:
    hands: [Hand] = [Hand(hand) for hand in hands]

    if len(hands) == 1:
        return [hands[0].original_input]
    elif len(hands) == 2:
        h1: Hand = hands[0]
        h2: Hand = hands[1]
        better_hand: Hand = h1.better_hand(h2)
        return [better_hand.original_input]
