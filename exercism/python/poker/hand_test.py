# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/poker/canonical-data.json
# File last updated on 2023-07-19

import unittest

from poker import (
    Hand, Card,
)


class HandTest(unittest.TestCase):

    def test_init_hand(self):
        init_hand: str = "3H 4H 5C 6C JD"
        hand: Hand = Hand(init_hand)
        self.assertEqual(init_hand, hand.original_input)
        self.assertEqual(Card("3H"), hand.cards[0])

    def test_hand_is_straight_flush(self):
        init_hand: str = "3S 4S 5S 6S 7S"
        hand: Hand = Hand(init_hand)
        self.assertTrue(hand.is_straight_flush)
        self.assertFalse(hand.is_flush, "flush detected, but it is straight flush")
        self.assertFalse(hand.is_straight)

    def test_hand_is_flush(self):
        init_hand: str = "2S 4S 5S 6S 7S"
        hand: Hand = Hand(init_hand)
        self.assertTrue(hand.is_flush)

    def test_hand_is_flush_negative_straight(self):
        init_hand: str = "3S 4S 5S 6S 7S"
        hand: Hand = Hand(init_hand)
        self.assertFalse(hand.is_flush)

    def test_hand_is_straight(self):
        init_hand: str = "3S 4D 2S 6D 5C"
        hand: Hand = Hand(init_hand)
        self.assertTrue(hand.is_straight)

    def test_hand_is_straight_ace_low(self):
        init_hand: str = "3S 4D 2S AD 5C"
        hand: Hand = Hand(init_hand)
        self.assertTrue(hand.is_straight)

    def test_hand_is_straight_ace_high(self):
        init_hand: str = "10S JD QS AD KC"
        hand: Hand = Hand(init_hand)
        self.assertTrue(hand.is_straight)

    def test_hand_is_straight_negative_flush(self):
        init_hand: str = "10S JS QS AS KS"
        hand: Hand = Hand(init_hand)
        self.assertFalse(hand.is_straight)

    def test_hand_has_given_card_rank(self):
        init_hand: str = "3S 4D 2S AD 5C"
        hand: Hand = Hand(init_hand)
        self.assertTrue(hand._has_given_card_rank("A"))

    def test_hand_is_grouped(self):
        init_hand: str = "2S 2C 2D 3H 3D"
        hand: Hand = Hand(init_hand)
        expected_grouping: dict = {
            "2" : 3,
            "3" : 2
        }
        self.assertEqual(expected_grouping, hand._group_cards())

    def test_hand_is_four_of_a_kind(self):
        init_hand: str = "2S 2C 2D 2H 3D"
        hand: Hand = Hand(init_hand)
        self.assertTrue(hand.is_four_of_a_kind)

    def test_hand_is_four_of_a_kind_negative(self):
        init_hand: str = "2S 2C 2D 3H 3D"
        hand: Hand = Hand(init_hand)
        self.assertFalse(hand.is_four_of_a_kind)

    def test_hand_is_full_house(self):
        init_hand: str = "2S 2C 2D 3H 3D"
        hand: Hand = Hand(init_hand)
        self.assertTrue(hand.is_full_house)

    def test_hand_is_full_house_negative(self):
        init_hand: str = "2S 2C 4D 3H 3D"
        hand: Hand = Hand(init_hand)
        self.assertFalse(hand.is_full_house)

    def test_hand_is_three_of_a_kind(self):
        init_hand: str = "QS QC QD AH KD"
        hand: Hand = Hand(init_hand)
        self.assertTrue(hand.is_three_of_a_kind)

    def test_hand_is_three_of_a_kind_negative_quads(self):
        init_hand: str = "QS QC QD QH KD"
        hand: Hand = Hand(init_hand)
        self.assertFalse(hand.is_three_of_a_kind)

    def test_hand_is_three_of_a_kind_negative_full_house(self):
        init_hand: str = "QS QC QD AH AD"
        hand: Hand = Hand(init_hand)
        self.assertFalse(hand.is_three_of_a_kind)

    def test_hand_is_two_pair(self):
        init_hand: str = "QS QC 10D 10H 2D"
        hand: Hand = Hand(init_hand)
        self.assertTrue(hand.is_two_pair)

    def test_hand_is_two_pair_negative_one_pair(self):
        init_hand: str = "QS QC 10D 9H 2D"
        hand: Hand = Hand(init_hand)
        self.assertFalse(hand.is_two_pair)

    def test_hand_is_one_pair(self):
        init_hand: str = "QS QC 10D 9H 2D"
        hand: Hand = Hand(init_hand)
        self.assertTrue(hand.is_one_pair)

    def test_hand_is_high_card(self):
        init_hand: str = "QS 3C 4D 5H 2D"
        hand: Hand = Hand(init_hand)
        self.assertTrue(hand.is_high_card)

    def test_hand_is_high_card_negative_straight(self):
        init_hand: str = "AS 2C 3D 4H 5D"
        hand: Hand = Hand(init_hand)
        self.assertFalse(hand.is_high_card)

    def test_get_pair_values_one_pair(self):
        init_hand: str = "3S 4H 6S 4D JH"
        hand: Hand = Hand(init_hand)
        expected_pairs = [4]
        self.assertEqual(expected_pairs, hand._get_pair_values())

    def test_get_pair_values_two_pairs(self):
        init_hand: str = "4H 4D JH 3S 3C"
        hand: Hand = Hand(init_hand)
        expected_pairs = [3, 4]
        self.assertEqual(expected_pairs, sorted(hand._get_pair_values()))

    def test_get_cards_without_set(self):
        init_hand: str = "6S 3S 4H 4D JH"
        hand: Hand = Hand(init_hand)
        cards_without_set = [3, 6, 11]
        self.assertEqual(cards_without_set, sorted(hand._get_cards_without_set()))

    def test_conversion_values_to_ranks(self):
        init_hand: str = "6S 3S 4H 4D JH"
        hand: Hand = Hand(init_hand)
        values_to_convert: [str]= ["6", "3", "J"]
        expected_ranks: [int] = [3, 6, 11]
        self.assertEqual(expected_ranks, sorted(hand._value_to_ranks(values_to_convert)))
