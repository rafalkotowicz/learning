def sanitize_input(sentence: str) -> str:
    to_be_removed: str = ' ."_0123456789'
    result: str = sentence
    for char in to_be_removed:
        result = result.replace(char, "")
    return result.lower()


def is_pangram(sentence: str) -> bool:
    return len(set(sanitize_input(sentence))) == 26
