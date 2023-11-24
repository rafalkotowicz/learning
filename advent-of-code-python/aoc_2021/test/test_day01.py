import unittest

from aoc_2021.src.day01 import get_depth_increases, get_depth_increases_window
from utils.common import read_and_sanitize


class TestSonarSweep(unittest.TestCase):
    def test_part1_example(self):
        expected_depth_increase = 7
        input: [str] = read_and_sanitize("resources/day1_example.txt")
        input: [int] = [int(x) for x in input]
        actual_depth_increase = get_depth_increases(input)
        self.assertEqual(expected_depth_increase, actual_depth_increase)

    def test_part1_puzzle(self):
        expected_depth_increase = 1195
        input: [str] = read_and_sanitize("resources/day1.txt")
        input: [int] = [int(x) for x in input]
        actual_depth_increase = get_depth_increases(input)
        self.assertEqual(expected_depth_increase, actual_depth_increase)

    def test_part2_example(self):
        expected_depth_increase = 5
        input: [str] = read_and_sanitize("resources/day1_example.txt")
        input: [int] = [int(x) for x in input]
        actual_depth_increase = get_depth_increases_window(input)
        self.assertEqual(expected_depth_increase, actual_depth_increase)

    def test_part2_puzzle(self):
        expected_depth_increase = 1235
        input: [str] = read_and_sanitize("resources/day1.txt")
        input: [int] = [int(x) for x in input]
        actual_depth_increase = get_depth_increases_window(input)
        self.assertEqual(expected_depth_increase, actual_depth_increase)


if __name__ == '__main__':
    unittest.main()
