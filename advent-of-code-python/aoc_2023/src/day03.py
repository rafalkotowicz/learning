# Entities: engine_schematic, part (number, positions), symbol
# solution: load schematic -> find parts -> check adjacency -> sum missing parts
# find gears: add '*' position and filter by it
class Part:
    value: int
    x_start: int
    x_end: int
    y: int
    is_engine_part: bool

    def __init__(self, value, x_s, x_e, y):
        self.value = value
        self.x_start = x_s
        self.x_end = x_e
        self.y = y
        self.is_engine_part = False
        self.gear_x = None
        self.gear_y = None

    def set_is_engine_part(self, y, x, symbol):
        self.is_engine_part = True
        if symbol == '*':
            self.set_gear(y, x)

    def set_gear(self, y, x):
        if self.gear_x is None and self.gear_y is None:
            self.gear_y = y
            self.gear_x = x
        elif self.gear_x == x and self.gear_y == y:
            pass
        else:
            print(f'[WARN] Second gear detected (part={self.value}, x={x}), y={y}')

    def __repr__(self):
        return (f'part:{self.value},({self.x_start}-{self.x_end},{self.y}),'
                f' is_engine_part:{self.is_engine_part}, gear: (x={self.gear_x},y={self.gear_y})')


def build_engine_schematic(input) -> []:
    engine_schematic: [str] = []
    for line in input:
        row: [int] = []
        for elem in list(line):
            row.append(elem)
        engine_schematic.append(row)
    return engine_schematic


def find_parts(schematic: [str]) -> [Part]:
    found: [Part] = []
    for y, row in enumerate(schematic):
        part: str = ''
        for x, elem in enumerate(row):
            if elem.isdigit():
                part += elem
            else:
                if part:
                    found.append(Part(int(part), x - len(part), x - 1, y))
                    part = ''
        if part:
            found.append(Part(int(part), x - len(part), x - 1, y))
            part = ''
    return found


def label_engine_parts(parts: [Part], schematic: []):
    rows, cols = len(schematic), len(schematic[0])

    for part in parts:
        y = part.y
        for x in range(part.x_start, part.x_end + 1):
            if y - 1 >= 0 and x - 1 >= 0:
                if is_symbol(schematic[y - 1][x - 1]):
                    part.set_is_engine_part(y - 1, x - 1, schematic[y - 1][x - 1])

            if y - 1 >= 0:
                if is_symbol(schematic[y - 1][x]):
                    part.set_is_engine_part(y - 1, x, schematic[y - 1][x])

            if y - 1 > 0 and x + 1 < cols:
                if is_symbol(schematic[y - 1][x + 1]):
                    part.set_is_engine_part(y - 1, x + 1, schematic[y - 1][x + 1])

            if x - 1 > 0:
                if is_symbol(schematic[y][x - 1]):
                    part.set_is_engine_part(y, x - 1, schematic[y][x - 1])

            if x + 1 < cols:
                if is_symbol(schematic[y][x + 1]):
                    part.set_is_engine_part(y, x + 1, schematic[y][x + 1])

            if y + 1 < rows and x - 1 >= 0:
                if is_symbol(schematic[y + 1][x - 1]):
                    part.set_is_engine_part(y + 1, x - 1, schematic[y + 1][x - 1])
                    pass

            if y + 1 < rows:
                if is_symbol(schematic[y + 1][x]):
                    part.set_is_engine_part(y + 1, x, schematic[y + 1][x])
                    pass

            if y + 1 < rows and x + 1 < cols:
                if is_symbol(schematic[y + 1][x + 1]):
                    part.set_is_engine_part(y + 1, x + 1, schematic[y + 1][x + 1])
                    pass


def is_symbol(character: str) -> bool:
    symbols: [str] = ['$', '-', '#', '&', '+', '/', '*', '@', '%', '=']
    return character in symbols


def sum_missing_engine_parts(input: [str]) -> int:
    engine_schematic: [str] = build_engine_schematic(input)
    parts: [Part] = find_parts(engine_schematic)
    label_engine_parts(parts, engine_schematic)

    return sum([part.value for part in parts if part.is_engine_part])


def find_by_gear_pos(potential_gears: [Part], x, y) -> (Part, Part):
    found: [Part] = []
    for part in potential_gears:
        if (part.gear_x, part.gear_y) == (x, y):
            found.append(part)
    return found[0], found[1]


def sum_of_gear_ratios(input: [str]) -> int:
    engine_schematic: [str] = build_engine_schematic(input)
    parts: [Part] = find_parts(engine_schematic)
    label_engine_parts(parts, engine_schematic)

    potential_gears: [Part] = [part for part in parts if part.gear_y]
    gears_centers_positions: (int, int) = [(part.gear_x, part.gear_y) for part in potential_gears]
    gear_centers_grouped = {gear_pos: gears_centers_positions.count(gear_pos) for gear_pos in
                            set(gears_centers_positions)}
    pairs: [] = []
    for part in potential_gears:
        if gear_centers_grouped[(part.gear_x, part.gear_y)] == 2:
            gears: (Part, Part) = find_by_gear_pos(potential_gears, part.gear_x, part.gear_y)
            pairs.append((gears[0].value, gears[1].value))

    return sum([pair[0] * pair[1] for pair in pairs]) // 2
