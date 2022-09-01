def is_valid(isbn: str) -> bool:
    sanitized_input: str = isbn.replace("-", "")

    if len(sanitized_input) != 10:
        return False

    digit_sum: int = 0
    for i in range(0, 10):
        curr: str = sanitized_input[i]
        if i < 9 and curr.isdigit():
            digit_sum += int(curr) * (10 - i)
        else:
            if curr.isdigit():
                digit_sum += int(curr)
            elif curr == "X":
                digit_sum += 10
            else:
                return False

    return digit_sum % 11 == 0
