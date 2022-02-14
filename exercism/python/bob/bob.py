def response(hey_bob: str) -> str:
    """
    Bob the lackadaisical teenager.
    :param hey_bob: str - message to Bob
    :return str - Bob's response
    """
    hey_bob = hey_bob.strip()

    if hey_bob.isupper():
        if hey_bob[-1] == "?":
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    elif len(hey_bob) == 0:
        return "Fine. Be that way!"
    elif hey_bob[-1] == "?":
        return "Sure."

    return "Whatever."
