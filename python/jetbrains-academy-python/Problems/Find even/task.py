N = int(input().strip())
i = 1
while i < N:
    if i % 2 == 1:
        i += 1
        continue
    print(i)
    i += 2
