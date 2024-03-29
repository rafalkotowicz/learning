import unittest

from poker import (
    best_hands,
)


class PokerTest(unittest.TestCase):
    def test_sane_one_pair_lowest_card_differs(self):
        self.assertEqual(
            best_hands(["3S 4H 6S 4D JH", "2S 4C 6C 4S JS"]), ["3S 4H 6S 4D JH"]
        )
