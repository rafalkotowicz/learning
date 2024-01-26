def decode(string: str) -> str:
    if len(string) == 0:
        return ""

    decoded = []
    occurrences = ""
    for char in string:
        if char.isdigit():
            occurrences += char
        elif occurrences:
            decoded.append(int(occurrences) * char)
            occurrences = ""
        else:
            decoded.append(char)

    return "".join(decoded)


def encode(string: str) -> str:
    if len(string) == 0:
        return ""

    encoded = []
    same_letters = 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            same_letters += 1
        else:
            encoded.append(str(same_letters) if same_letters > 1 else "")
            encoded.append(string[i - 1])
            same_letters = 1

    encoded.append(str(same_letters) if same_letters > 1 else "")
    encoded.append(string[-1])

    return "".join(encoded)
