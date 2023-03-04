def find(search_list: list, value: int) -> int:
    start: int = 0
    end: int = len(search_list)

    while start != end:
        position: int = (start + end) // 2
        if search_list[position] == value:
            return position
        elif (end - start) <= 1:
            break
        elif search_list[position] > value:
            end = position
        else:
            start = position

    raise ValueError("value not in array")
