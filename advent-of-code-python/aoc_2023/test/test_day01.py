import unittest

from aoc_2023.src.day01 import calculate_calilbration, calculate_calilbration_2
from utils.common import read_and_sanitize


class TestDay01Part01(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_init_state(self):
        expected_value = 142
        input: [str] = read_and_sanitize("resources/day01example.txt")
        actual_value = calculate_calilbration(input)
        self.assertEqual(expected_value, actual_value)

    def test_puzzle_1(self):
        expected_value = 55029
        input: [str] = read_and_sanitize("resources/day01puzzle.txt")
        actual_value = calculate_calilbration(input)
        self.assertEqual(expected_value, actual_value)


class TestDay01Part02(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_init_state(self):
        expected_value = 281
        input: [str] = read_and_sanitize("resources/day01example2.txt")
        actual_value = calculate_calilbration_2(input)
        self.assertEqual(expected_value, actual_value)

    # 55680 - too low
    def test_puzzle_2(self):
        expected_value = 55686
        input: [str] = read_and_sanitize("resources/day01puzzle.txt")
        actual_value = calculate_calilbration_2(input)
        self.assertEqual(expected_value, actual_value)


if __name__ == '__main__':
    unittest.main()
