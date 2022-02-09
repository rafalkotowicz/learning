EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time: int):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int):
    """Calculate time needed to prepare based on number of layers

    :param number_of_layers: number of layers of the lasagna
    :return: estimated preparation time
    """
    return number_of_layers * 2


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
    """Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the time already spent
    baking and calculates the total elapsed minutes spent cooking the lasagna.

    :param number_of_layers: number of layers
    :param elapsed_bake_time: elapsed time in oven
    :return: total elapsed minutes spent cooking the lasagna
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
