# Before looking at Solutions:
# given = input().strip()
# out = []
# x1, x2 = 0, 0
# for i in given:
#     x1 = x2
#     x2 = int(i)
#     if i == given[0]:
#         continue
#     out.append((x1 + x2) / 2)
# print(out)
# After looking at Solutions:
digits = [int(d) for d in input().strip()]
print([(digits[x] + digits[x + 1]) / 2 for x in range(len(digits) - 1)])
