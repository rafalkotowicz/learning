import string


def rows(letter: str) -> [str]:
    if letter == "A":
        return ["A"]
    result: [str] = []
    max = string.ascii_uppercase.index(letter)
    for i, l in enumerate(list(string.ascii_uppercase)):
        if l == "A":
            result.append(f"{' ' * (max - i)}{l}{' ' * (max - i)}")
        else:
            result.append(f"{' ' * (max - i)}{l}{' ' * (2 * i - 1)}{l}{' ' * (max - i)}")
        if l == letter:
            break

    for i in range(len(result)):
        current = result[max - i - 1]
        result.append(current)
        if "A" in current:
            break

    return result
