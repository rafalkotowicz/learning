import unittest

from src.day15 import ESS, Sensor, Beacon, Node, SensorArea, calculate_tuning_frequency
from utils.common import read_and_sanitize


class TestTestSensorsPart1(unittest.TestCase):

    def setUp(self) -> None:
        self.ESS = ESS()

    def tearDown(self) -> None:
        self.ESS = None

    def test_parse_one_line_of_input(self):
        intput_line = 'Sensor at x=2, y=18: closest beacon is at x=-2, y=15\n'
        self.ESS.load_1_line(intput_line)
        self.assertEqual(intput_line, self.ESS.__str__())

    def test_comparing_sensors_and_beacons(self):
        intput_line = 'Sensor at x=2, y=18: closest beacon is at x=-2, y=15\n'
        self.ESS.load_1_line(intput_line)
        actual_sensor = self.ESS.sensors_with_beacons[0][0]
        actual_beacon = self.ESS.sensors_with_beacons[0][1]
        self.assertIsInstance(actual_sensor, Sensor)
        self.assertIsInstance(actual_beacon, Beacon)
        expected_sensor = Sensor(2, 18)
        expected_beacon = Beacon(-2, 15)
        self.assertEqual(expected_sensor, actual_sensor)
        self.assertEqual(expected_beacon, actual_beacon)

    def test_Manhattan_distance(self):
        intput_line = 'Sensor at x=2, y=18: closest beacon is at x=-2, y=15\n'
        self.ESS.load_1_line(intput_line)
        actual_sensor: Sensor = self.ESS.sensors_with_beacons[0][0]
        actual_beacon: Beacon = self.ESS.sensors_with_beacons[0][1]
        self.assertEqual(7, actual_sensor.get_Manhattan_distance(actual_beacon))

    def test_Manhattan_distance(self):
        intput_line = 'Sensor at x=8, y=7: closest beacon is at x=2, y=10\n'
        self.ESS.load_1_line(intput_line)
        actual_sensor: Sensor = self.ESS.sensors_with_beacons[0][0]
        actual_beacon: Beacon = self.ESS.sensors_with_beacons[0][1]
        self.assertEqual(9, actual_sensor.get_Manhattan_distance(actual_beacon))

    def test_get_nodes_withing_range(self):
        node = Node(8, 7)
        self.assertEqual(19, len(node.get_nodes_within_distance_on_y(9, 7)))

    def test_filter_by_y(self):
        node = Node(8, 7)
        self.assertEqual(1, len(node.get_nodes_within_distance_on_y(9, -2)))
        self.assertEqual(19, len(node.get_nodes_within_distance_on_y(9, 7)))
        self.assertEqual(17, len(node.get_nodes_within_distance_on_y(9, 8)))
        self.assertEqual(15, len(node.get_nodes_within_distance_on_y(9, 9)))
        self.assertEqual(13, len(node.get_nodes_within_distance_on_y(9, 10)))
        self.assertEqual(11, len(node.get_nodes_within_distance_on_y(9, 11)))
        self.assertEqual(1, len(node.get_nodes_within_distance_on_y(9, 16)))

    def test_load_14_sensors(self):
        lines = read_and_sanitize('../test/resources/day15_test.txt')
        self.ESS.load_many_lines(lines)
        self.assertEqual(14, len(self.ESS.sensors_with_beacons))

    def test_unavailable_beacons(self):
        lines = read_and_sanitize('../test/resources/day15_test.txt')
        self.ESS.load_many_lines(lines)
        self.assertEqual(25, len(self.ESS.beacon_impossible_y(9)))
        self.assertEqual(26, len(self.ESS.beacon_impossible_y(10)))
        self.assertEqual(27, len(self.ESS.beacon_impossible_y(11)))


class TestSensorsPart1(unittest.TestCase):

    def setUp(self) -> None:
        self.ESS = ESS()

    def tearDown(self) -> None:
        self.ESS = None

    def test_line_2000000(self):
        lines = read_and_sanitize('../test/resources/day15.txt')
        self.ESS.load_many_lines(lines)
        self.assertEqual(26, len(self.ESS.sensors_with_beacons))
        y = 2_000_000
        # print(len(self.ESS.beacon_impossible_y(y)))
        self.assertEqual(5176944, len(self.ESS.beacon_impossible_y(y)))


class TestTestSensorsPart2(unittest.TestCase):

    def setUp(self) -> None:
        self.ESS = ESS()

    def tearDown(self) -> None:
        self.ESS = None

    def test_sensor_area(self):
        sensor_area: SensorArea = SensorArea(8, 7, 9)
        sensor_area.create_area()
        self.assertEqual((8, 8), sensor_area.area[-2])
        self.assertEqual((7, 9), sensor_area.area[-1])
        self.assertEqual((6, 10), sensor_area.area[0])
        self.assertEqual((-1, 17), sensor_area.area[7])
        self.assertEqual((8, 8), sensor_area.area[16])

    def test_find_distress_beacon(self):
        lines = read_and_sanitize('../test/resources/day15_test.txt')
        self.ESS.load_many_lines(lines)
        self.assertEqual(14, len(self.ESS.sensors_with_beacons))
        self.ESS.calculate_areas()
        self.assertEqual(14, len(self.ESS.sensor_areas))
        self.assertEqual((14, 11), self.ESS.find_distress_beacon(20))


class TestSensorsPart2(unittest.TestCase):

    def setUp(self) -> None:
        self.ESS = ESS()

    def tearDown(self) -> None:
        self.ESS = None

    def test_find_distress_beacon(self):
        lines = read_and_sanitize('../test/resources/day15.txt')
        self.ESS.load_many_lines(lines)
        self.assertEqual(26, len(self.ESS.sensors_with_beacons))
        self.ESS.calculate_areas()
        self.assertEqual(26, len(self.ESS.sensor_areas))
        (x,y) = (self.ESS.find_distress_beacon(4_000_000))
        print((x,y))
        print((calculate_tuning_frequency(x,y)))
        # self.assertEqual(5176944, len(self.ESS.beacon_impossible_y(y)))

    # 4_783_168_000_000(L)
    #21_482_900_008_734(H)
    def test_calculate_tuning_frequency(self):
        print(calculate_tuning_frequency(1195792, 0))


if __name__ == '__main__':
    unittest.main()
