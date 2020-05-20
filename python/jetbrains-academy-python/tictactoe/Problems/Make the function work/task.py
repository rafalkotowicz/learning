def closest_mod_5(x):
    if x % 5 == 0:
        return x
    return [i + x for i in range(1, 5) if (x + i) % 5 == 0][0]
