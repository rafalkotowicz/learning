def transpose(lines: str) -> [str]:
    lines: [str] = lines.split("\n")
    max_length: int = max(len(line) for line in lines)
    transposed: [str] = []

    for col, line in enumerate(lines):
        if col == 0:
            if len(line) < max_length:
                line = line + " " * (max_length - len(line))
            transposed.extend(list(line))
        else:
            for row, char in enumerate(list(line)):
                if len(transposed[row]) < col:
                    missing_chars: int = col - len(transposed[row])
                    transposed[row] += f"{' ' * missing_chars}{char}"
                else:
                    transposed[row] += char

    return "\n".join(transposed)
