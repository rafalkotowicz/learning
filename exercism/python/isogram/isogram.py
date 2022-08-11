def is_isogram(string: str) -> bool:
    string = string.replace("-", "").replace(" ", "").lower()
    return len(string) == len(set(string))
