import re


def commands(binary_str: str) -> str:
    secret_handshake: [] = []
    if re.match("....1", binary_str):
        secret_handshake.append("wink")
    if re.match("...1.", binary_str):
        secret_handshake.append("double blink")
    if re.match("..1..", binary_str):
        secret_handshake.append("close your eyes")
    if re.match(".1...", binary_str):
        secret_handshake.append("jump")
    if re.match("1....", binary_str):
        secret_handshake.reverse()

    return secret_handshake
