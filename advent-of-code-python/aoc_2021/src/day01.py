def get_depth_increases(depth: [int]) -> int:
    prev = depth[0]
    increase_count = 0
    for current in depth:
        if current > prev:
            increase_count += 1
        prev = current

    return increase_count


def get_depth_increases_window(depth: [int]) -> int:
    windows: [int] = [depth[i] + depth[i + 1] + depth[i + 2] for i in range(len(depth) - 2)]
    return get_depth_increases(windows)
