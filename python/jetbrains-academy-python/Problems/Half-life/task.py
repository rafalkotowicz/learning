N = int(input().strip())
R = int(input().strip())

half_time = 12
iterations = 0

while R < N:
    N /= 2
    iterations += 1

print(iterations * half_time)
