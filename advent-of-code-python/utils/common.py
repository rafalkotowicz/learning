
def read_and_sanitize(path) -> [str]:
    with open(path) as f:
        lines = f.readlines()
        lines = [line.replace('\n', '') for line in lines]
    return lines

def read_one_line(path) -> str:
    return read_and_sanitize(path)[0]