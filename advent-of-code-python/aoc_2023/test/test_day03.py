import unittest

from aoc_2023.src._day03 import build_engine_schematic, Part, find_parts, sum_missing_engine_parts, label_engine_parts, \
    sum_of_gear_ratios
from utils.common import read_and_sanitize


class TestDay03Part01(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_build_engine_schematic(self):
        expected_value = (10, 10)
        input: [str] = read_and_sanitize('resources/day03example.txt')
        engine_schematic: [str] = build_engine_schematic(input)
        actual_rows = len(engine_schematic)
        actual_cols = len(engine_schematic[0])
        # [print(row) for row in engine_schematic]
        self.assertEqual(expected_value, (actual_rows, actual_cols))

    def test_find_parts(self):
        expected_value = 10
        input: [str] = read_and_sanitize('resources/day03example.txt')
        engine_schematic: [str] = build_engine_schematic(input)
        parts: [Part] = find_parts(engine_schematic)
        actual_value = len(parts)
        # [print(part) for part in parts]
        self.assertEqual(expected_value, actual_value)

    def test_label_engine_parts(self):
        expected_value = 8
        input: [str] = read_and_sanitize('resources/day03example.txt')
        engine_schematic: [str] = build_engine_schematic(input)
        parts: [Part] = find_parts(engine_schematic)
        label_engine_parts(parts, engine_schematic)
        actual_value = len([part for part in parts if part.is_engine_part])
        # [print(part) for part in parts]
        self.assertEqual(expected_value, actual_value)

    def test_example(self):
        expected_value = 4361
        input: [str] = read_and_sanitize('resources/day03example.txt')
        actual_value = sum_missing_engine_parts(input)
        self.assertEqual(expected_value, actual_value)

    # 532422 is too low
    def test_puzzle(self):
        expected_to_be_more_than = 532422
        expected_value = 535235
        input: [str] = read_and_sanitize('resources/day03puzzle.txt')
        actual_value = sum_missing_engine_parts(input)
        self.assertTrue(actual_value > expected_to_be_more_than,
                        f'actual: {actual_value}, should be more than: {expected_to_be_more_than}')
        self.assertEqual(expected_value, actual_value)


class TestDay03Part02(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_example(self):
        expected_value = 467835
        input: [str] = read_and_sanitize('resources/day03example.txt')
        actual_value = sum_of_gear_ratios(input)
        self.assertEqual(expected_value, actual_value)

    # 79725552 is too low
    def test_puzzle(self):
        expected_value = 467835
        input: [str] = read_and_sanitize('resources/day03puzzle.txt')
        actual_value = sum_of_gear_ratios(input)
        self.assertEqual(expected_value, actual_value)
        self.assertTrue(actual_value > 79725552, "Must be more than 79725552")


if __name__ == '__main__':
    unittest.main()
