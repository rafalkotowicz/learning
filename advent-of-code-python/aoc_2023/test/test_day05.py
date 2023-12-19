import unittest

from aoc_2023.src._day05 import lowest_location_number, parse_input, map_once, build_seed_ranges, is_in_range, \
    get_overlapping_range, get_mapped_range, map_range_once
from utils.common import read_and_sanitize


class TestDay05Part01(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_parse_input(self) -> None:
        expected_seeds: [int] = [79, 14, 55, 13]
        expected_maps: [[int]] = [
            [(50, 98, 2), (52, 50, 48)],
            [(0, 15, 37), (37, 52, 2), (39, 0, 15)],
            [(49, 53, 8), (0, 11, 42), (42, 0, 7), (57, 7, 4)],
            [(88, 18, 7), (18, 25, 70)],
            [(45, 77, 23), (81, 45, 19), (68, 64, 13)],
            [(0, 69, 1), (1, 0, 69)],
            [(60, 56, 37), (56, 93, 4)]
        ]
        input: [str] = read_and_sanitize('resources/day05example.txt')
        actual_seeds, actual_maps = parse_input(input)
        self.assertEqual(expected_seeds, actual_seeds)
        self.assertEqual(expected_maps, actual_maps)

    def test_map_once(self) -> None:
        input_nums: [int] = [79, 14, 55, 13]
        mappings: [(int, int, int)] = [(50, 98, 2), (52, 50, 48)]
        expected_nums: [int] = [81, 14, 57, 13]
        actual_mapped_nums: [int] = map_once(mappings, input_nums)
        self.assertEqual(expected_nums, actual_mapped_nums)

    def test_example(self):
        expected = 35
        input: [str] = read_and_sanitize('resources/day05example.txt')
        actual = lowest_location_number(input)
        self.assertEqual(expected, actual)

    def test_example(self):
        expected = 403695602
        input: [str] = read_and_sanitize('resources/day05puzzle.txt')
        actual = lowest_location_number(input)
        self.assertEqual(expected, actual)


class TestDay05Part02(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_build_seed_ranges(self):
        seeds_input: [int] = [79, 14, 55, 13]
        expected_seeds_ranges: [(int, int)] = [(79, 92), (55, 67)]
        actual_seeds_ranges: [(int, int)] = build_seed_ranges(seeds_input)
        self.assertEqual(expected_seeds_ranges, actual_seeds_ranges)

    def test_is_in_range(self):
        self.assertTrue(is_in_range((10, 20), (10, 20)))
        self.assertTrue(is_in_range((0, 10), (10, 20)))
        self.assertTrue(is_in_range((20, 25), (10, 20)))
        self.assertTrue(is_in_range((0, 50), (10, 20)))
        self.assertTrue(is_in_range((12, 15), (10, 20)))
        self.assertTrue(is_in_range((12, 30), (10, 20)))
        self.assertTrue(is_in_range((3, 15), (10, 20)))

    def test_get_overlapping_range(self):
        self.assertEqual((10, 20), get_overlapping_range((10, 20), (10, 20)))
        self.assertEqual((10, 10), get_overlapping_range((0, 10), (10, 20)))
        self.assertEqual((20, 20), get_overlapping_range((20, 25), (10, 20)))
        self.assertEqual((10, 20), get_overlapping_range((0, 50), (10, 20)))
        self.assertEqual((12, 15), get_overlapping_range((12, 15), (10, 20)))
        self.assertEqual((12, 20), get_overlapping_range((12, 30), (10, 20)))
        self.assertEqual((10, 15), get_overlapping_range((3, 15), (10, 20)))

    def test_get_mapped_range(self):
        self.assertEqual((8, 18), get_mapped_range((10, 20), -2))
        self.assertEqual((13, 23), get_mapped_range((10, 20), +3))

    def test_map_range_once(self):
        input_ranges: [(int, int)] = [(79, 92), (55, 67)]
        input_map: [(int, int, int)] = [(50, 98, 2), (52, 50, 48)]
        expected_mapped_range: [(int, int)] = [(0,0), (0,0)]
        actual_mapped_range: [(int, int)] = map_range_once(input_map, input_ranges)

        self.assertEqual(expected_mapped_range, actual_mapped_range)


if __name__ == '__main__':
    unittest.main()
