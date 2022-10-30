import re


class FoundLine:

    def __init__(self, line, filename, line_number):
        self.line = line
        self.filename = filename
        self.line_number = line_number

    def get_line(self, flags: str) -> str:
        result: str = ""
        if "-f" in flags:
            result += self.filename + ":"
        if "-n" in flags:
            result += str(self.line_number) + ":"
        result += self.line
        return result


def read_file(filename: str) -> [str]:
    with open(filename) as file:
        return file.readlines()


def grep(pattern: str, flags: str, files: [str]) -> str:
    matched: [FoundLine] = []
    not_matched: [FoundLine] = []

    if "-x" in flags:
        pattern = f"^{pattern}$"

    ignore_flag = 0
    if "-i" in flags:
        ignore_flag = re.IGNORECASE

    for file in files:
        lines = read_file(file)
        for line_number, line in enumerate(lines):
            if re.search(pattern, line, flags=ignore_flag):
                matched.append(FoundLine(line, file, line_number + 1))
            else:
                not_matched.append(FoundLine(line, file, line_number + 1))

    print_flags = ""
    if len(files) > 1:
        print_flags += "-f "

    results = not_matched if "-v" in flags else matched

    if "-l" in flags:
        files_matched = set([item.filename for item in results])
        result = "".join([file + "\n" for file in files if file in files_matched])
    elif "-n" in flags:
        print_flags += "-n "
        result = "".join([item.get_line(print_flags) for item in results])
    else:
        result = "".join([item.get_line(print_flags) for item in results])

    return result
