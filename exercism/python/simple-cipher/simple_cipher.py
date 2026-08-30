"""Simple Vigenere cipher implementation used by Exercism tests."""

from secrets import choice
from string import ascii_lowercase


class Cipher:
    """Encode and decode lowercase text with a lowercase substitution key."""

    def __init__(self, key=None):
        self.key = self._build_key(key)

    def encode(self, text):
        """Return ciphertext created by shifting text with this instance key."""
        return self._transform(text, is_encode=True)

    def decode(self, text):
        """Return plaintext created by unshifting text with this instance key."""
        return self._transform(text, is_encode=False)

    @staticmethod
    def _build_key(key):
        if key is None:
            return "".join(choice(ascii_lowercase) for _ in range(100))

        if not key.isalpha() or not key.islower():
            raise ValueError("Key must contain lowercase letters only")

        return key

    def _transform(self, text, *, is_encode):
        transformed_letters = []
        key_length = len(self.key)

        for letter_index, plaintext_letter in enumerate(text):
            key_letter = self.key[letter_index % key_length]
            shift_distance = ord(key_letter) - ord("a")
            letter_position = ord(plaintext_letter) - ord("a")

            shifted_position = (
                (letter_position + shift_distance) % 26
                if is_encode
                else (letter_position - shift_distance) % 26
            )

            transformed_letters.append(chr(ord("a") + shifted_position))

        return "".join(transformed_letters)
