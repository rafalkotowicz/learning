import unittest

from resistor_color_duo import (
    value,
)


# Tests adapted from `problem-specifications//canonical-data.json`


class ResistorColorDuoTest(unittest.TestCase):
    def test_brown_and_black(self):
        self.assertEqual(10, value(["brown", "black"]))

    def test_blue_and_grey(self):
        self.assertEqual(68, value(["blue", "grey"]))

    def test_yellow_and_violet(self):
        self.assertEqual(47, value(["yellow", "violet"]))

    def test_white_and_red(self):
        self.assertEqual(92, value(["white", "red"]))

    def test_orange_and_orange(self):
        self.assertEqual(33, value(["orange", "orange"]))

    def test_ignore_additional_colors(self):
        self.assertEqual(51, value(["green", "brown", "orange"]))

    def test_black_and_brown_one_digit(self):
        self.assertEqual(1, value(["black", "brown"]))
