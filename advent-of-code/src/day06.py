with open('day06.txt') as f:
    line = f.readline()


# PART 1 & 2
def start_of_packet_marker(signal: str, window_size: int) -> int:
    window_begin = 0
    window_end = window_begin + window_size

    while window_end < len(signal):
        slice = signal[window_begin:window_end]
        if window_size == len(set(slice)):
            return window_end
        window_begin += 1
        window_end = window_begin + window_size


assert start_of_packet_marker('bvwbjplbgvbhsrlpgdmjqwftvncz', 4) == 5
assert start_of_packet_marker('nppdvjthqldpwncqszvftbrmjlhg', 4) == 6
assert start_of_packet_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 4) == 10
assert start_of_packet_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 4) == 11
print(start_of_packet_marker(line, 4))
print(start_of_packet_marker(line, 14))
