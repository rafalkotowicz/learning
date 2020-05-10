N = int(input().strip())

factorial = 1
i = 1

while i <= N:
    factorial *= i
    i += 1

print(factorial)
