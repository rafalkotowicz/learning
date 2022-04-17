def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    # I tried list comprehension, but I still find simple loop more readable.
    # count = 0
    # for index, elem in enumerate(strand_a):
    #     if elem != strand_b[index]:
    #         count += 1

    return len([index for index, elem in enumerate(strand_a) if elem != strand_b[index]])
