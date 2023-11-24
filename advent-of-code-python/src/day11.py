from functools import reduce


class Monkey:
    def __init__(self, worry_levels: [int], operation, test, if_true, if_false):
        self._worry_levels: [int] = worry_levels
        self._operation = operation
        self._test = test
        self._if_true = if_true
        self._if_false = if_false
        self._inspected_items = 0


class MonkeyGame:
    def __init__(self, monkeys: [Monkey], manage_worry):
        self._monkeys: [Monkey] = monkeys
        self._done_rounds: int = 0
        self._manage_worry = manage_worry

    def do_1_turn(self, monkey: Monkey):
        worry_levels_copy = monkey._worry_levels.copy()
        for worry in worry_levels_copy:
            monkey._worry_levels.remove(worry)
            worry = self.do_1_inspection(monkey, worry)
            if monkey._test(worry):
                self._monkeys[monkey._if_true]._worry_levels.append(worry)
            else:
                self._monkeys[monkey._if_false]._worry_levels.append(worry)

    def do_1_inspection(self, monkey: Monkey, worry):
        new_worry = monkey._operation(worry)
        monkey._inspected_items += 1
        return self._manage_worry(new_worry)

    def do_rounds(self, rounds: int = 1):
        for _round in range(rounds):
            for monkey in self._monkeys:
                self.do_1_turn(monkey)
            self._done_rounds += 1
            # print(f'{_round}. M_0 inspect: {self._monkeys[0]._inspected_items}, M_0 worries: {self._monkeys[0]._worry_levels}')

    def load_monkeys(self):
        pass

    def get_2_most_active_monkeys(self):
        inspected_items = [monkey._inspected_items for monkey in self._monkeys]
        inspected_items.sort(reverse=True)
        return inspected_items[:2]

    def get_monkey_business(self):
        return reduce((lambda x, y: x * y), self.get_2_most_active_monkeys())
