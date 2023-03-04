import string


def cipher_one_char(char: str, key: int) -> str:
    is_upper: bool = char.isupper()
    char: str = char.lower()
    current_pos: int = string.ascii_lowercase.find(char)
    new_pos: int = (current_pos + key) % 26
    return string.ascii_lowercase[new_pos].upper() if is_upper else string.ascii_lowercase[new_pos]


def rotate(text: str, key: int) -> str:
    ciphered: str = ""

    for char in text:
        if char.isalpha():
            ciphered += cipher_one_char(char, key)
        else:
            ciphered += char
    return ciphered
