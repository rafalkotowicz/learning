n = int(input().strip())
winners = []
for _i in range(n):
    row = input()
    if row.find("win") != -1:
        winners.append(row.replace(" win", ""))

print(winners)
print(len(winners))
