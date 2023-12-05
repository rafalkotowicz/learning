import unittest

from aoc_2023.src.day04 import parse_one_line, find_hits, scratchard_worth, scratchards_won, read_cards, Card
from utils.common import read_and_sanitize


class TestDay04Part01(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_parse_one_line(self):
        expected_value = (1, [41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53])
        actual_value = parse_one_line("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", 5)
        self.assertEqual(expected_value, actual_value)

    def test_parse_one_line(self):
        expected_card = 1
        expected_winning = [34, 55, 49, 53, 46, 7, 82, 22, 59, 33]
        expected_guesses = [33, 29, 7, 66, 22, 51, 59, 21, 55, 85, 53, 26, 94, 46, 24, 82, 6, 47, 38, 2, 34, 89, 49, 41,
                            76]
        actual_card, actual_winning, actual_guesses = parse_one_line(
            "Card   1: 34 55 49 53 46  7 82 22 59 33 | 33 29  7 66 22 51 59 21 55 85 53 26 94 46 24 82  6 47 38  2 34 89 49 41 76",
            10)
        self.assertEqual(expected_card, actual_card)
        self.assertEqual(expected_winning, actual_winning)
        self.assertEqual(expected_guesses, actual_guesses)

    def test_find_hits(self):
        expected_value = [48, 83, 17, 86]
        actual_value = find_hits([41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53])
        self.assertEqual(set(expected_value), set(actual_value))

    def test_example(self):
        input: [str] = read_and_sanitize('resources/day04example.txt')
        expected_value = 13
        actual_value = scratchard_worth(input, 5)
        self.assertEqual(expected_value, actual_value)

    def test_puzzle(self):
        input: [str] = read_and_sanitize('resources/day04puzzle.txt')
        expected_value = 21959
        actual_value = scratchard_worth(input, 10)
        self.assertLess(actual_value, 703264)
        self.assertEqual(expected_value, actual_value)


class TestDay04Part02(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_read_cards(self) -> None:
        input: [str] = read_and_sanitize('resources/day04example.txt')
        cards: [Card] = read_cards(input, 5)
        self.assertEqual(6, len(cards))
        self.assertEqual(4, cards[0].hits)
        self.assertEqual(2, cards[1].hits)
        self.assertEqual(2, cards[2].hits)
        self.assertEqual(1, cards[3].hits)
        self.assertEqual(0, cards[4].hits)
        self.assertEqual(1, cards[1].copies)

    def test_example(self):
        input: [str] = read_and_sanitize('resources/day04example.txt')
        expected_value = 30
        actual_value = scratchards_won(input, 5)
        self.assertEqual(expected_value, actual_value)

    def test_puzzle(self):
        input: [str] = read_and_sanitize('resources/day04puzzle.txt')
        expected_value = 5132675
        actual_value = scratchards_won(input, 10)
        self.assertEqual(expected_value, actual_value)


if __name__ == '__main__':
    unittest.main()
