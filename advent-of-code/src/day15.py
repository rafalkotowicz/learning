import re
import time


class Node:
    def __init__(self, x: str, y: str):
        self.x: int = int(x)
        self.y: int = int(y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __hash__(self):
        return hash((self.x, self.y))

    def get_Manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def get_nodes_within_distance_on_y(self, dxy, on_y) -> set:
        within_range: [Node] = set()
        for dx in range(-dxy, dxy + 1):
            tmp_node = Node(self.x + dx, on_y)
            if self.get_Manhattan_distance(tmp_node) <= dxy:
                within_range.add(tmp_node)
        return within_range


class Sensor(Node):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)


class SensorArea:
    def __init__(self, x: int, y: int, dist: int):
        self.x = int(x)
        self.y = int(y)
        self.dist = dist
        self.area: {int: (int, int)} = None

    def create_area(self) -> None:
        area: {int: (int, int)} = dict()
        width = 0
        for dy in range(-self.dist, self.dist + 1):
            area[self.y + dy] = (self.x - width, self.x + width)
            if self.y + dy < self.y:
                width += 1
            else:
                width -= 1
        self.area = area

    def __repr__(self):
        return f'({self.x},{self.y}) = {self.area}'


class Beacon(Node):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)


class ESS:
    def __init__(self):
        self.sensors_with_beacons: [(Sensor, Beacon)] = []
        self.sensor_areas: [SensorArea] = []

    def load_1_line(self, line: str) -> None:
        sanitized = re.sub(':|,|x=|y=', '', line)
        split = sanitized.split()
        self.sensors_with_beacons.append((Sensor(split[2], split[3]), Beacon(split[8], split[9])))

    def load_many_lines(self, lines: [str]) -> None:
        [self.load_1_line(line) for line in lines]

    def beacon_impossible_y(self, on_y):
        result: set[Node] = set()
        for id, (sensor, beacon) in enumerate(self.sensors_with_beacons):
            distance = sensor.get_Manhattan_distance(beacon)
            nodes_on_y = sensor.get_nodes_within_distance_on_y(distance, on_y)
            result.update(nodes_on_y)
            # print(f'Sensor id: {id}, Nodes on y: {len(nodes_on_y)}')

        sensors = [sensor for sensor, _ in self.sensors_with_beacons]
        beacons = [beacon for _, beacon in self.sensors_with_beacons]
        result.difference_update(sensors)
        result.difference_update(beacons)
        return result

    def calculate_areas(self) -> None:
        for id, (sensor, beacon) in enumerate(self.sensors_with_beacons):
            distance = sensor.get_Manhattan_distance(beacon)
            sa = SensorArea(sensor.x, sensor.y, distance)
            sa.create_area()
            self.sensor_areas.append(sa)

    def find_distress_beacon(self, max_size) -> (int, int):
        start_time = time.time()
        in_areas = False
        # for y in range(0, max_size + 1):
        #     for x in range(0, max_size + 1):
        #         for sensor_area in self.sensor_areas:
        #             if y in sensor_area.area.keys():
        #                 x_start, x_end = sensor_area.area.get(y)
        #                 if x_start <= x <= x_end:
        #                     x = x_end
        #                     in_areas = True
        #                 if x >= max_size:
        #                     break
        #         if in_areas:
        #             in_areas = False
        #         else:
        #             return x, y
        x,y = (0,0)
        while True:
            for sensor_area in self.sensor_areas:
                if y in sensor_area.area.keys():
                    x_start, x_end = sensor_area.area.get(y)
                    if x_start <= x <= x_end:
                        x = x_end
                    # if x > max_size:
                    #     break
            if x<= max_size and y<=max_size:
                    return x, y

            if y % 10_000 == 0:
                print(f'x={x}, y={y}, {time.time() - start_time}s passed')
            y+=1
            x=0



    def __str__(self):
        result: str = ''
        for s, b in self.sensors_with_beacons:
            result += f'Sensor at x={s.x}, y={s.y}: closest beacon is at x={b.x}, y={b.y}'
            result += '\n'
        return result


def calculate_tuning_frequency(x, y) -> int:
    return x * 4_000_000 + y
