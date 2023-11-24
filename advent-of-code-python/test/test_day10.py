import unittest
from unittest.mock import MagicMock

from src.day10 import CPU
from utils.common import read_and_sanitize


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.cpu = CPU()

    def tearDown(self) -> None:
        self.cpu = None

    def test_cpu_load_instructions(self):
        expected = ['noop', 'addx 3', 'addx -5']
        self.cpu.store_instructions(expected)
        self.assertSequenceEqual(expected, self.cpu.instructions)

    def test_tick_updated_cycle_counter(self):
        self.cpu.load_instruction = MagicMock(name='process_instruction')
        self.cpu.tick(20)
        self.assertEqual(20, self.cpu.cycle_counter)
        self.cpu.tick(40)
        self.assertEqual(60, self.cpu.cycle_counter)
        self.cpu.tick(40)
        self.assertEqual(100, self.cpu.cycle_counter)

    def test_register_starts_at_1(self):
        self.assertEqual(1, self.cpu.register)

    def test_getting_one_instruction(self):
        self.cpu.store_instructions(['noop', 'addx 3', 'addx -5'])
        self.assertEqual(self.cpu.get_one_instruction(), 'noop')
        self.assertEqual(self.cpu.get_one_instruction(), 'addx 3')
        self.assertEqual(self.cpu.get_one_instruction(), 'addx -5')

    def test_3_instructions(self):
        self.cpu.store_instructions(['noop', 'addx 3', 'addx -5'])
        self.cpu.tick(1)
        self.assertEqual(self.cpu.register, 1)
        self.cpu.tick(1)
        self.assertEqual(self.cpu.register, 1)
        self.cpu.tick(1)
        self.assertEqual(self.cpu.register, 4)
        self.cpu.tick(1)
        self.assertEqual(self.cpu.register, 4)
        self.cpu.tick(1)
        self.assertEqual(self.cpu.register, -1)

    def test_register_values_146_instructions(self):
        instructions = read_and_sanitize('../test/resources/day10_test.txt')
        self.cpu.store_instructions(instructions)
        self.assertEqual(len(self.cpu.instructions), 146)
        self.cpu.tick(19)
        self.assertEqual(self.cpu.register, 21)
        self.cpu.tick(40)
        self.assertEqual(self.cpu.register, 19)
        self.cpu.tick(40)
        self.assertEqual(self.cpu.register, 18)
        self.cpu.tick(40)
        self.assertEqual(self.cpu.register, 21)
        self.cpu.tick(40)
        self.assertEqual(self.cpu.register, 16)
        self.cpu.tick(40)
        self.assertEqual(self.cpu.register, 18)

    def test_signal_strength_146_instructions(self):
        instructions = read_and_sanitize('../test/resources/day10_test.txt')
        self.cpu.store_instructions(instructions)
        self.assertEqual(len(self.cpu.instructions), 146)
        expected: [(int, int)] = [
            (20, 420),
            (40, 1140),
            (40, 1800),
            (40, 2940),
            (40, 2880),
            (40, 3960)
        ]
        for ticks, expected_signal_strength in expected:
            self.cpu.tick(ticks)
        self.assertEqual(self.cpu.signal_strength, expected_signal_strength)

if __name__ == '__main__':
    unittest.main()
