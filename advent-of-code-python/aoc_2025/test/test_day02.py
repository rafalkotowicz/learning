import unittest

from aoc_2025.src.day02 import puzzle_1
from utils.common import read_one_line


class TestDay02Part01(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_init_state(self):
        actual = puzzle_1(read_one_line('aoc_2025/test/resources/day02example.txt'))
        expected = 1227775554
        self.assertEqual(expected, actual)

    def test_puzzle_1(self):
        actual = puzzle_1(read_one_line('aoc_2025/test/resources/day02puzzle.txt'))
        expected = 35367539282
        self.assertEqual(expected, actual)


class TestDay02Part02(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_init_state(self):
        pass

    def test_puzzle_2(self):
        pass

if __name__ == '__main__':
    unittest.main()
