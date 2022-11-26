import math


def encode(message: str, rails: int) -> str:
    encoded: [str] = [''] * rails
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
    rail_lengths: [int] = [0]*rails
    window = 2 * rails - 2
    decoded_message: str = ''
    # cut encoded_message into pieces -> rail_lengths

    for id in range(len(encoded_message)):
        if id % window < rails:
            # print(f'id: {id}, rail: {id % window}, letter: {letter}')
            decoded_message += rail_lengths[id % window]
        else:
            # print(f'id: {id}, rail: {-(id % window - window // 2)}, letter: {letter}')
            decoded_message += rail_lengths[-(id % window - window // 2) - 1]



    return decoded_message
