from utils.common import read_and_sanitize

main_puzzle = read_and_sanitize('../test/resources/day10.txt')
test_puzzle = read_and_sanitize('../test/resources/day10_test.txt')


class Buffer():
    def __init__(self, instruction, finish_cycle):
        self._instruction = instruction
        self._finish_cycle = finish_cycle

    def __repr__(self) -> str:
        return f'Instruction: {self._instruction}, Finish at cycle: {self._finish_cycle}'


class CPU:

    def __init__(self):
        self.cycle_counter: int = 0
        self.register: int = 1
        self.instructions: [str] = []
        self.buffer = None
        self.signal_strength = 0
        self.built_in_graphics = [[] for i in range(6)]

    def store_instructions(self, new_instructions: [int] = None) -> None:
        if new_instructions is not None:
            self.instructions.extend(new_instructions)

    def get_one_instruction(self):
        return self.instructions.pop(0)

    def tick(self, number_of_ticks: int) -> None:
        for i in range(number_of_ticks):
            self.signal_strength = self.register * (self.cycle_counter + 1)
            self.crt_update()
            self.load_instruction()
            self.cycle_counter += 1

    def load_instruction(self) -> None:
        if self.buffer is not None:
            if self.buffer._finish_cycle == self.cycle_counter + 1:
                self.process_instruction(self.buffer._instruction, True)
            else:
                return
        else:
            self.process_instruction(self.get_one_instruction(), False)

    def process_instruction(self, instruction: str, from_buffer: bool):
        if instruction == 'noop':
            return
        if instruction.startswith('addx'):
            if from_buffer:
                self.addx(instruction)
                self.buffer = None
            else:
                self.buffer = Buffer(instruction, self.cycle_counter + 2)

    def addx(self, instruction) -> None:
        _, value = instruction.split()
        self.register += int(value)

    def crt_update(self):
        sprite = [self.register - 1, self.register, self.register + 1]
        row = self.cycle_counter // 40
        if self.cycle_counter - row * 40 in sprite:
            self.built_in_graphics[row].append('#')
        else:
            self.built_in_graphics[row].append('.')

    def __repr__(self) -> str:
        return f'Cycle: {self.cycle_counter}, Registers: {self.register}' \
               f' Buffer: {self.buffer}, Signal Strength: {self.signal_strength}'


def part_1_solution():
    cpu = CPU()
    cpu.store_instructions(main_puzzle)
    signals_strength: [int] = []
    cpu.tick(20)
    signals_strength.append(cpu.signal_strength)
    for i in range(5):
        cpu.tick(40)
        signals_strength.append(cpu.signal_strength)
    print(sum(signals_strength))


# part_1_solution()


def part_2_test():
    cpu = CPU()
    cpu.store_instructions(test_puzzle)
    for i in range(240):
        cpu.tick(1)
    [print(''.join(row)) for row in cpu.built_in_graphics]


# part_2_test()

# Part 2, K
def part_2_solution():
    cpu = CPU()
    cpu.store_instructions(main_puzzle)
    for i in range(240):
        cpu.tick(1)
    [print('-'.join(row)) for row in cpu.built_in_graphics]


# part_2_solution()
