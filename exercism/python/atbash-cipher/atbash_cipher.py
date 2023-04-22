import re
import string


def _sanitize_input(plain_text: str) -> str:
    plain_text = plain_text.lower()
    return re.sub(r"[\ ,.]", "", plain_text)


def slice_string_by_5(text: str) -> str:
    sliced: [str] = []
    for i, character in enumerate(list(text)):
        sliced.append(character)
        if i >= 4 and (i + 1) % 5 == 0:
            sliced.append(" ")

    return "".join(sliced).strip()


def encode(plain_text: str) -> str:
    return __encode_decode(plain_text, True)


def decode(ciphered_text: str) -> str:
    return __encode_decode(ciphered_text, False)


def __encode_decode(text: str, encode: bool) -> str:
    sanitized_text: str = _sanitize_input(text)
    translated: list[str] = []
    key: str = string.ascii_lowercase[::-1]

    for id, character in enumerate(list(sanitized_text)):
        if character.isalpha():
            translated.append(key[string.ascii_lowercase.find(character)])
        else:
            translated.append(character)

    translated = "".join(translated)

    if encode:
        translated = slice_string_by_5(translated)

    return translated
