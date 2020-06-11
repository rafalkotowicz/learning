from random import seed, randint

n = int(input())

seed(n)
print(randint(-100, 100))
