import re


def abbreviate(words: str) -> str:
    return ''.join(word[0].upper() for word in re.findall(r"[a-zA-Z']+", words))
