def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    result: set[int] = set()
    for i in range(limit):
        for multiple in multiples:
            if multiple == 0:
                continue
            if i % multiple == 0:
                result.add(i)
    return sum(result)
