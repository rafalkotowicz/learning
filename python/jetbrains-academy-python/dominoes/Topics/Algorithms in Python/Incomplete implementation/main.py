def startswith_capital_counter(names):
    count = 0
    for name in names:
        # if str(name).startswith(("A", "B", "C", "E", "F", "G",
        #                          "H", "I", "J", "K", "L", "M",
        #                          "N", "O", "P", "Q", "R", "S",
        #                          "T", "U", "V", "X", "Y", "Z")):
        if str(name).istitle():
            count += 1

    return count
