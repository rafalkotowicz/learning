def encode(numbers: list) -> list:
    encoded = []
    for number in numbers:
        bytes_ = []
        while number > 0:
            bytes_.insert(0, number & 0x7F)
            number >>= 7
        if not bytes_:
            bytes_.append(0)
        for i in range(len(bytes_) - 1):
            bytes_[i] |= 0x80
        encoded.extend(bytes_)
    return encoded


def decode(bytes_: list) -> list:
    decoded = []
    current = 0
    for byte in bytes_:
        current = (current << 7) | (byte & 0x7F)
        if byte & 0x80 == 0:
            decoded.append(current)
            current = 0
    if bytes_ and bytes_[-1] & 0x80 != 0:
        raise ValueError("incomplete sequence")
    return decoded
