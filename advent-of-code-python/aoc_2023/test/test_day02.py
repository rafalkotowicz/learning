import unittest

from aoc_2023.src.day02 import find_game_prefix, extract_game_id, remove_game_prefix, possible_games, \
    possible_games_2
from utils.common import read_and_sanitize


class TestDay02Part01(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_cut_out_game_prefix(self):
        expected_value = 'Game 22:'
        actual_value = find_game_prefix('Game 22: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue')
        self.assertEqual(expected_value, actual_value)

    def test_extract_game_id(self):
        expected_value = 22
        actual_value = extract_game_id('Game 22:')
        self.assertEqual(expected_value, actual_value)

    def test_remove_game_prefix(self):
        expected_value = '1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue'
        actual_value = remove_game_prefix('Game 22: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue')
        self.assertEqual(expected_value, actual_value)

    def test_example(self):
        expected_value = 8
        input: [str] = read_and_sanitize('resources/day02example.txt')
        actual_value = possible_games(input, 12, 13, 14)
        self.assertEqual(expected_value, actual_value)

    def test_puzle(self):
        expected_value = 2331
        input: [str] = read_and_sanitize('resources/day02puzzle.txt')
        actual_value = possible_games(input, 12, 13, 14)
        self.assertEqual(expected_value, actual_value)


class TestDay02Part02(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_example(self):
        expected_value = 2286
        input: [str] = read_and_sanitize('resources/day02example.txt')
        actual_value = possible_games_2(input)
        self.assertEqual(expected_value, actual_value)

    def test_puzzle(self):
        expected_value = 71585
        input: [str] = read_and_sanitize('resources/day02puzzle.txt')
        actual_value = possible_games_2(input)
        self.assertEqual(expected_value, actual_value)


if __name__ == '__main__':
    unittest.main()
