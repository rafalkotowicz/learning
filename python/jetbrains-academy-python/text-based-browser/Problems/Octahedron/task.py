import math

side = int(input())
area = 2 * math.sqrt(3) * math.pow(side, 2)
volume = 1 / 3 * 2 ** (1 / 2) * side ** 3
print(str(round(area, 2)) + " " + str(round(volume, 2)))
