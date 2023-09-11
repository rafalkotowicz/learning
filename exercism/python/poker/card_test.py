import unittest

from poker import (
    Card,
)


class HandTest(unittest.TestCase):

    def test_init_card(self):
        init_card: str = "3H"
        card: Card = Card(init_card)
        self.assertEqual("3", card.value)
        self.assertEqual("H", card.suit)

    def test_init_card_10(self):
        init_card: str = "10H"
        card: Card = Card(init_card)
        self.assertEqual("10", card.value)
        self.assertEqual("H", card.suit)
