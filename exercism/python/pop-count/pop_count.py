def egg_count(display_value: int) -> int:
    current_value: int = display_value
    reversed_binary: [int] = []
    while current_value > 0:
        if current_value % 2 == 0:
            reversed_binary.append(0)
        else:
            reversed_binary.append(1)
        current_value //= 2

    return sum(reversed_binary)
