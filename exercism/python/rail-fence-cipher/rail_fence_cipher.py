import math


def encode(message: str, rails: int) -> str:
    encoded: [[str]] = [''] * rails
    window = 2 * rails - 2

    for id, letter in enumerate(message):
        if id % window < rails:
            # print(f'id: {id}, rail: {id % window}, letter: {letter}')
            encoded[id % window] += letter
        else:
            # print(f'id: {id}, rail: {-(id % window - window // 2)}, letter: {letter}')
            encoded[-(id % window - window // 2) - 1] += letter

    return "".join(encoded)


def decode(encoded_message: str, rails: int) -> str:
    pass
