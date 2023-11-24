import unittest
from functools import reduce

from aoc_2022.src.day11 import Monkey, MonkeyGame


class Test4MonkeysPart1(unittest.TestCase):

    def setUp(self) -> None:
        times_19 = lambda x: x * 19
        divisible_by_23 = lambda x: x % 23 == 0
        self.monkey_0: Monkey = Monkey([79, 98], times_19, divisible_by_23, 2, 3)
        plus_6 = lambda x: x + 6
        divisible_by_19 = lambda x: x % 19 == 0
        self.monkey_1: Monkey = Monkey([54, 65, 75, 74], plus_6, divisible_by_19, 2, 0)
        square = lambda x: x * x
        divisible_by_13 = lambda x: x % 13 == 0
        self.monkey_2: Monkey = Monkey([79, 60, 97], square, divisible_by_13, 1, 3)
        plus_3 = lambda x: x + 3
        divisible_by_17 = lambda x: x % 17 == 0
        self.monkey_3: Monkey = Monkey([74], plus_3, divisible_by_17, 0, 1)
        manage_worry = lambda x: x // 3
        self.mokey_game: MonkeyGame = MonkeyGame([self.monkey_0, self.monkey_1,
                                                  self.monkey_2, self.monkey_3],
                                                 manage_worry)

    def tearDown(self) -> None:
        self.mokey_game = None
        self.monkey_0 = None

    def test_monkey_init_state(self):
        self.assertIsInstance(self.monkey_0, Monkey)
        self.assertEqual(38, self.monkey_0._operation(2))
        self.assertTrue(self.monkey_0._test(46))
        self.assertFalse(self.monkey_0._test(45))
        self.assertEqual(2, self.monkey_0._if_true)
        self.assertEqual(3, self.monkey_0._if_false)
        self.assertEqual(0, self.monkey_0._inspected_items)

    def test_divide_by_3(self):
        self.assertEqual(1, self.mokey_game._manage_worry(4))
        self.assertEqual(1, self.mokey_game._manage_worry(5))

    def test_state_after_1st_round(self):
        self.mokey_game.do_rounds(1)
        self.assertEqual(self.mokey_game._done_rounds, 1)
        self.assertSequenceEqual([20, 23, 27, 26], self.mokey_game._monkeys[0]._worry_levels)
        self.assertSequenceEqual([2080, 25, 167, 207, 401, 1046], self.mokey_game._monkeys[1]._worry_levels)

    def test_state_after_20th_round(self):
        self.mokey_game.do_rounds(20)
        self.assertEqual(self.mokey_game._done_rounds, 20)
        self.assertSequenceEqual([10, 12, 14, 26, 34], self.mokey_game._monkeys[0]._worry_levels)
        self.assertSequenceEqual([245, 93, 53, 199, 115], self.mokey_game._monkeys[1]._worry_levels)
        self.assertEqual(101, self.mokey_game._monkeys[0]._inspected_items)
        self.assertEqual(105, self.mokey_game._monkeys[3]._inspected_items)
        self.assertEqual([105, 101], self.mokey_game.get_2_most_active_monkeys())
        self.assertEqual(10605, self.mokey_game.get_monkey_business())


class Test4MonkeysPart2(unittest.TestCase):

    def setUp(self) -> None:
        times_19 = lambda x: x * 19
        divisible_by_23 = lambda x: x % 23 == 0
        self.monkey_0: Monkey = Monkey([79, 98], times_19, divisible_by_23, 2, 3)
        plus_6 = lambda x: x + 6
        divisible_by_19 = lambda x: x % 19 == 0
        self.monkey_1: Monkey = Monkey([54, 65, 75, 74], plus_6, divisible_by_19, 2, 0)
        square = lambda x: x * x
        divisible_by_13 = lambda x: x % 13 == 0
        self.monkey_2: Monkey = Monkey([79, 60, 97], square, divisible_by_13, 1, 3)
        plus_3 = lambda x: x + 3
        divisible_by_17 = lambda x: x % 17 == 0
        self.monkey_3: Monkey = Monkey([74], plus_3, divisible_by_17, 0, 1)
        multiply_divisors = reduce((lambda x, y: x * y), [23, 19, 13, 17])
        manage_worry = lambda x: x % multiply_divisors
        self.monkey_game: MonkeyGame = MonkeyGame([self.monkey_0, self.monkey_1,
                                                   self.monkey_2, self.monkey_3],
                                                  manage_worry)

    def tearDown(self) -> None:
        self.monkey_game = None
        self.monkey_0 = None

    def test_state_after_10000th_round(self):
        self.monkey_game.do_rounds(10000)
        self.assertEqual(10000, self.monkey_game._done_rounds)
        self.assertEqual(52166, self.monkey_game._monkeys[0]._inspected_items)
        self.assertEqual(52013, self.monkey_game._monkeys[3]._inspected_items)
        self.assertEqual([52166, 52013], self.monkey_game.get_2_most_active_monkeys())
        self.assertEqual(2713310158, self.monkey_game.get_monkey_business())


class TestPart1Solution(unittest.TestCase):
    def setUp(self) -> None:
        m_0 = Monkey([74, 64, 74, 63, 53], lambda x: x * 7, lambda x: x % 5 == 0, 1, 6)
        m_1 = Monkey([69, 99, 95, 62], lambda x: x * x, lambda x: x % 17 == 0, 2, 5)
        m_2 = Monkey([59, 81], lambda x: x + 8, lambda x: x % 7 == 0, 4, 3)
        m_3 = Monkey([50, 67, 63, 57, 63, 83, 97], lambda x: x + 4, lambda x: x % 13 == 0, 0, 7)
        m_4 = Monkey([61, 94, 85, 52, 81, 90, 94, 70], lambda x: x + 3, lambda x: x % 19 == 0, 7, 3)
        m_5 = Monkey([69], lambda x: x + 5, lambda x: x % 3 == 0, 4, 2)
        m_6 = Monkey([54, 55, 58], lambda x: x + 7, lambda x: x % 11 == 0, 1, 5)
        m_7 = Monkey([79, 51, 83, 88, 93, 76], lambda x: x * 3, lambda x: x % 2 == 0, 0, 6)
        manage_worry = lambda x: x // 3
        self.monkey_game = MonkeyGame([m_0, m_1, m_2, m_3, m_4, m_5, m_6, m_7], manage_worry)

    def tearDown(self) -> None:
        self.monkey_game = None

    def test_part_1(self):
        self.monkey_game.do_rounds(20)
        print(self.monkey_game.get_2_most_active_monkeys())
        print(self.monkey_game.get_monkey_business())


class TestPart2Solution(unittest.TestCase):
    def setUp(self) -> None:
        m_0 = Monkey([74, 64, 74, 63, 53], lambda x: x * 7, lambda x: x % 5 == 0, 1, 6)
        m_1 = Monkey([69, 99, 95, 62], lambda x: x * x, lambda x: x % 17 == 0, 2, 5)
        m_2 = Monkey([59, 81], lambda x: x + 8, lambda x: x % 7 == 0, 4, 3)
        m_3 = Monkey([50, 67, 63, 57, 63, 83, 97], lambda x: x + 4, lambda x: x % 13 == 0, 0, 7)
        m_4 = Monkey([61, 94, 85, 52, 81, 90, 94, 70], lambda x: x + 3, lambda x: x % 19 == 0, 7, 3)
        m_5 = Monkey([69], lambda x: x + 5, lambda x: x % 3 == 0, 4, 2)
        m_6 = Monkey([54, 55, 58], lambda x: x + 7, lambda x: x % 11 == 0, 1, 5)
        m_7 = Monkey([79, 51, 83, 88, 93, 76], lambda x: x * 3, lambda x: x % 2 == 0, 0, 6)
        multiply_divisors = reduce((lambda x, y: x * y), [5, 17, 7, 13, 19, 3, 11, 2])
        manage_worry = lambda x: x % multiply_divisors
        self.monkey_game = MonkeyGame([m_0, m_1, m_2, m_3, m_4, m_5, m_6, m_7], manage_worry)

    def tearDown(self) -> None:
        self.monkey_game = None

    def test_part_2(self):
        self.monkey_game.do_rounds(10000)
        print(self.monkey_game.get_2_most_active_monkeys())
        print(self.monkey_game.get_monkey_business())


class TestDynamicallyLoadedMonkeys(unittest.TestCase):

    def test_loading_monkeys_from_file(self):
        pass


if __name__ == '__main__':
    unittest.main()
