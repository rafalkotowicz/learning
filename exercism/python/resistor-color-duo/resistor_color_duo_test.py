import unittest

from resistor_color_duo import (
    actual,
)


# Tests adapted from `problem-specifications//canonical-data.json`


class ResistorColorDuoTest(unittest.TestCase):
    def test_brown_and_black(self):
        self.assertEqual(10, actual(["brown", "black"]))

    def test_blue_and_grey(self):
        self.assertEqual(68, actual(["blue", "grey"]))

    def test_yellow_and_violet(self):
        self.assertEqual(47, actual(["yellow", "violet"]))

    def test_white_and_red(self):
        self.assertEqual(92, actual(["white", "red"]))

    def test_orange_and_orange(self):
        self.assertEqual(33, actual(["orange", "orange"]))

    def test_ignore_additional_colors(self):
        self.assertEqual(51, actual(["green", "brown", "orange"]))

    def test_black_and_brown_one_digit(self):
        self.assertEqual(1, actual(["black", "brown"]))
