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


# PART 2 Game plan
# * build seed ranges
# * sort mapping ranges
# * process ranges: ranges 1--->*  mapped_ranges
# * combine ranges after mapping? (probably not needed)
#
# adapt along the way :)

def build_seed_ranges(seeds: [int]) -> [(int, int)]:
    seed_ranges: [(int, int)] = []
    for id in range(0, len(seeds), 2):
        if 0 <= id + 1 < len(seeds):
            range_start = seeds[id]
            range_end = range_start + seeds[id + 1] - 1
            seed_ranges.append((range_start, range_end))
    return seed_ranges


def is_in_range(mapping: (int, int), in_range: (int, int)) -> bool:
    return in_range[0] <= mapping[0] <= in_range[1] or in_range[0] <= mapping[1] <= in_range[1] or \
        mapping[0] <= in_range[0] and mapping[1] >= in_range[1]


def get_overlapping_range(mapping: (int, int), in_range: (int, int)) -> (int, int):
    start, end = -1, -1
    if in_range[0] <= mapping[0] <= in_range[1]:
        start = mapping[0]
    else:
        start = in_range[0]
    if in_range[0] <= mapping[1] <= in_range[1]:
        end = mapping[1]
    else:
        end = in_range[1]

    return start, end


def get_mapped_range(overlapping_range, change):
    return overlapping_range[0] + change, overlapping_range[1] + change


def map_range_once(mappings: [(int, int, int)], input_ranges: [(int, int)]):
    mapped_ranges: [(int, int)] = []
    sorted_mappings = sorted(mappings, key=lambda x: x[1])

    for input_range in input_ranges:
        for mapping in sorted_mappings:
            map_start = mapping[1]
            map_end = map_start + mapping[2]
            map_dst = mapping[0]
            map_change = map_dst - map_start
            if input_range[0] < map_start :


    return mapped_ranges


def lowest_location_number_seed_ranges(lines: str) -> int:
    seeds, maps = parse_input(lines)
    seed_ranges: [(int, int)] = build_seed_ranges(seeds)
