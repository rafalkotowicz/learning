import re


def parse_one_line(line: str) -> (int, int, int):
    nums = [int(x) for x in line.split(' ')]
    return (nums[0], nums[1], nums[2])


def parse_input(lines: [str]) -> ([int], [[(int, int, int)]]):
    seeds: [int] = []
    seed_to_soil: [(int, int, int)] = []
    soil_to_fertilizer: [(int, int, int)] = []
    fertilizer_to_water: [(int, int, int)] = []
    water_to_light: [(int, int, int)] = []
    light_to_temperature: [(int, int, int)] = []
    temperature_to_humidity: [(int, int, int)] = []
    humidity_to_location: [(int, int, int)] = []
    sts, stf, ftw, wtl, ltt, tth, htl = [False, False, False, False, False, False, False]

    for line in lines:
        if line.startswith('seeds: '):
            seeds = [int(x) for x in (re.findall(r'(\d+)', line))]
        elif line == '':
            sts, stf, ftw, wtl, ltt, tth, htl = [False, False, False, False, False, False, False]
        elif line == 'seed-to-soil map:':
            sts = True
        elif sts:
            seed_to_soil.append(parse_one_line(line))
        elif line == 'soil-to-fertilizer map:':
            stf = True
        elif stf:
            soil_to_fertilizer.append(parse_one_line(line))
        elif line == 'fertilizer-to-water map:':
            ftw = True
        elif ftw:
            fertilizer_to_water.append(parse_one_line(line))
        elif line == 'water-to-light map:':
            wtl = True
        elif wtl:
            water_to_light.append(parse_one_line(line))
        elif line == 'light-to-temperature map:':
            ltt = True
        elif ltt:
            light_to_temperature.append(parse_one_line(line))
        elif line == 'temperature-to-humidity map:':
            tth = True
        elif tth:
            temperature_to_humidity.append(parse_one_line(line))
        elif line == 'humidity-to-location map:':
            htl = True
        elif htl:
            humidity_to_location.append(parse_one_line(line))

    return seeds, [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature,
                   temperature_to_humidity, humidity_to_location]


def map_once(mappings: [(int, int, int)], input_nums: [int]):
    mapped: [int] = []

    for in_num in input_nums:
        map_found = False
        for mapping in mappings:
            start = mapping[1]
            end = start + mapping[2] - 1
            dst = mapping[0]
            change = dst - start
            if start <= in_num <= end:
                mapped.append(in_num + change)
                map_found = True
                break
        if not map_found:
            mapped.append(in_num)

    return mapped


def lowest_location_number(lines: str) -> int:
    seeds, maps = parse_input(lines)
    current_numbers = seeds

    for cur_map in maps:
        current_numbers = map_once(cur_map, current_numbers)

    return min(current_numbers)
