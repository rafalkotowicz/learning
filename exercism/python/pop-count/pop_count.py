def egg_count(display_value: int) -> int:
    return sum(decimal_to_binart(display_value))


def decimal_to_binart(decimal: int) -> [int]:
    reversed_binary: [int] = []
    while decimal > 0:
        if decimal % 2 == 0:
            reversed_binary.append(0)
        else:
            reversed_binary.append(1)
        decimal //= 2

    reversed_binary.reverse()
    return reversed_binary
