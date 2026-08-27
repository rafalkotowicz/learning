def _rail_at(position: int, rails: int) -> int:
    if rails == 1:
        return 0
    window = 2 * rails - 2
    offset = position % window
    return offset if offset < rails else window - offset


def encode(message: str, rails: int) -> str:
    encoded: list[str] = [""] * rails
    for position, letter in enumerate(message):
        encoded[_rail_at(position, rails)] += letter
    return "".join(encoded)


def decode(encoded_message: str, rails: int) -> str:
    if not encoded_message or rails == 1:
        return encoded_message

    rail_lengths: list[int] = [0] * rails
    for position in range(len(encoded_message)):
        rail_lengths[_rail_at(position, rails)] += 1

    rail_chunks: list[str] = []
    chunk_start = 0
    for rail_length in rail_lengths:
        rail_chunks.append(encoded_message[chunk_start: chunk_start + rail_length])
        chunk_start += rail_length

    rail_offsets: list[int] = [0] * rails
    decoded: list[str] = []
    for position in range(len(encoded_message)):
        rail = _rail_at(position, rails)
        decoded.append(rail_chunks[rail][rail_offsets[rail]])
        rail_offsets[rail] += 1

    return "".join(decoded)
