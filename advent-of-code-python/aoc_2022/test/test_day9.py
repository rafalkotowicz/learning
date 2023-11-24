import unittest

from aoc_2022.src.day09 import process_input, is_tail_moving
from utils.common import read_and_sanitize


class MyTestCase(unittest.TestCase):
    def test_is_tail_moving_negative(self):
        self.assertFalse(is_tail_moving((1, 1), (2, 2)))
        self.assertFalse(is_tail_moving((1, 1), (0, 2)))
        self.assertFalse(is_tail_moving((1, 1), (1, 2)))
        self.assertFalse(is_tail_moving((1, 1), (0, 1)))

    def test_is_tail_moving_positive(self):
        self.assertTrue(is_tail_moving((1, 1), (0, 3)))
        self.assertTrue(is_tail_moving((1, 1), (-1, 2)))
        self.assertTrue(is_tail_moving((1, 1), (0, -1)))

    def test_R4(self):
        expected = [
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            [4, 3, 2, 1, 'H', '.']
        ]
        actual = process_input(['R 4'])
        self.assertEqual(expected, actual)

    def test_R4_U4(self):
        expected = [
            ['.', '.', '.', '.', 'H', '.'],
            ['.', '.', '.', '.', 1, '.'],
            ['.', '.', 4, 3, 2, '.'],
            ['.', 5, '.', '.', '.', '.'],
            [6, '.', '.', '.', '.', '.']
        ]
        actual = process_input(['R 4', 'U 4'])
        self.assertEqual(expected, actual)

    def test_R4_U4_L3(self):
        expected = [
            ['.', 'H', 1, '.', '.', '.'],
            ['.', '.', '.', 2, '.', '.'],
            ['.', '.', 4, 3, '.', '.'],
            ['.', 5, '.', '.', '.', '.'],
            [6, '.', '.', '.', '.', '.']
        ]
        actual = process_input(['R 4', 'U 4', 'L 3'])
        self.assertEqual(expected, actual)

    def test_small_final(self):
        expected = [
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', 1, 'H', 3, '.', '.'],
            ['.', 5, '.', '.', '.', '.'],
            [6, '.', '.', '.', '.', '.']
        ]
        lines = read_and_sanitize('resources/day09_test.txt')
        actual = process_input(lines)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
