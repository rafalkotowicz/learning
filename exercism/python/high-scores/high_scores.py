def latest(scores: list[int]) -> int:
    """
    Return last added score.

    @param scores: list[int] : high score list
    @return: lastly added score
    """
    return scores[-1]


def personal_best(scores: list[int]) -> int:
    """
    Return personal best
    @param scores: list[int] : high score list
    @return: the best score
    """
    return sorted(scores, reverse=True)[0]


def personal_top_three(scores: list[int]) -> int:
    """
    Return 3 highest scores
    @param scores: list[int] : high score list
    @return: 3 highest scores
    """
    return sorted(scores)[-1:-4:-1]
    # return sorted(scores, reverse=True)[0:3] #this works, just wanted to play
    #                                           with negative indexes.
