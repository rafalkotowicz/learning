a = int(input())
b = int(input())

curr = a;
divisible_by_3 = []
while curr <= b:
    if curr % 3 == 0:
        divisible_by_3.append(curr)
        curr += 3
    else:
        curr += 1
print(sum(divisible_by_3) / len(divisible_by_3))
