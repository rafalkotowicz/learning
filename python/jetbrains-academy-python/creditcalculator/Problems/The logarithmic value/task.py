from math import e, log

a = int(input())
b = int(input())

if b <= 0 or b == 1:
    # print(round(log1p(a), 2))
    print(round(log(a, e), 2))
else:
    print(round(log(a, b), 2))
