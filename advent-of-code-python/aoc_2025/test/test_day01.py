import unittest

from aoc_2025.src.day01 import puzzle_1, puzzle_2, puzzle_1_1
from utils.common import read_and_sanitize


class TestDay01Part01(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_init_state(self):
        instructions = read_and_sanitize('aoc_2025/test/resources/day01example.txt')
        actual_value = puzzle_1(instructions)
        expected_value = 3
        self.assertEqual(expected_value, actual_value)

    def test_puzzle_1(self):
        instructions = read_and_sanitize('aoc_2025/test/resources/day01puzzle.txt')
        actual_value = puzzle_1(instructions)
        expected_value = 999
        self.assertEqual(expected_value, actual_value)

    def test_puzzle_1_1(self):
        instructions = read_and_sanitize('aoc_2025/test/resources/day01puzzle.txt')
        actual_value = puzzle_1_1(instructions)
        expected_value = 999
        self.assertEqual(expected_value, actual_value)




class TestDay01Part02(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_init_state(self):
        instructions = read_and_sanitize('aoc_2025/test/resources/day01example.txt')
        actual_value = puzzle_2(instructions)
        expected_value = 6
        self.assertEqual(expected_value, actual_value)

    def test_puzzle_2(self):
        instructions = read_and_sanitize('aoc_2025/test/resources/day01puzzle.txt')
        actual_value = puzzle_2(instructions)
        print(actual_value)
        # expected_value = 999
        # self.assertEqual(expected_value, actual_value)

        #6104 is too high
        #6002 is too low


if __name__ == '__main__':
    unittest.main()
