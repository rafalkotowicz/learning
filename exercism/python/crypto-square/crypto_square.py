"""Implementation of the Exercism Crypto Square cipher."""


def cipher_text(plain_text):
    """Normalize plaintext and return its Crypto Square ciphertext."""
    normalized_text = "".join(
        character.lower()
        for character in plain_text
        if character.isalnum()
    )

    if not normalized_text:
        return ""

    character_count = len(normalized_text)
    column_count = 1
    while column_count * column_count < character_count:
        column_count += 1

    row_count = (character_count + column_count - 1) // column_count
    row_slices = [
        normalized_text[row_start:row_start + column_count]
        for row_start in range(0, character_count, column_count)
    ]

    encoded_chunks = []
    for column_index in range(column_count):
        chunk_characters = []
        for row_index in range(row_count):
            row_text = row_slices[row_index]
            if column_index < len(row_text):
                chunk_characters.append(row_text[column_index])
            else:
                chunk_characters.append(" ")
        encoded_chunks.append("".join(chunk_characters))

    return " ".join(encoded_chunks)
