"""Affine Cipher implementation."""

from math import gcd

ALPHABET_SIZE = 26
ENCODE_BLOCK_SIZE = 5
ASCII_LOWERCASE_A = ord("a")


def _validate_coprime(coefficient_a: int) -> None:
    if gcd(coefficient_a, ALPHABET_SIZE) != 1:
        raise ValueError("a and m must be coprime.")


def _encode_character(character: str, coefficient_a: int, coefficient_b: int) -> str:
    character_code = ord(character) - ASCII_LOWERCASE_A
    encoded_code = (
        (coefficient_a * character_code + coefficient_b) % ALPHABET_SIZE
    ) + ASCII_LOWERCASE_A
    return chr(encoded_code)


def _modular_inverse(number: int, modulo: int) -> int:
    return pow(number, -1, modulo)


def _decode_character(character: str, coefficient_a: int, coefficient_b: int) -> str:
    inverse_a = _modular_inverse(coefficient_a, ALPHABET_SIZE)
    character_code = ord(character) - ASCII_LOWERCASE_A
    decoded_code = (
        inverse_a * (character_code - coefficient_b) % ALPHABET_SIZE
    ) + ASCII_LOWERCASE_A
    return chr(decoded_code)


def encode(plain_text: str, coefficient_a: int, coefficient_b: int) -> str:
    """Encodes plain text using the affine cipher and groups the result in blocks of 5 characters."""
    _validate_coprime(coefficient_a)
    normalized_text = plain_text.lower()
    encoded_characters: list[str] = []

    for character in normalized_text:
        if character.isalpha():
            encoded_characters.append(
                _encode_character(character, coefficient_a, coefficient_b)
            )
        elif character.isdigit():
            encoded_characters.append(character)

    grouped_characters: list[str] = []
    for index in range(0, len(encoded_characters), ENCODE_BLOCK_SIZE):
        grouped_characters.append(
            "".join(encoded_characters[index : index + ENCODE_BLOCK_SIZE])
        )

    return " ".join(grouped_characters)


def decode(ciphered_text: str, coefficient_a: int, coefficient_b: int) -> str:
    """Decodes text encrypted with the affine cipher to a form without spaces."""
    _validate_coprime(coefficient_a)
    decoded_characters: list[str] = []

    for character in ciphered_text.lower():
        if character.isalpha():
            decoded_characters.append(
                _decode_character(character, coefficient_a, coefficient_b)
            )
        elif character.isdigit():
            decoded_characters.append(character)

    return "".join(decoded_characters)
