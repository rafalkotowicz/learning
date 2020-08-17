import math

x = int(input())
result = math.exp(x) / (math.exp(x) + 1)
print(round(result, 2))
