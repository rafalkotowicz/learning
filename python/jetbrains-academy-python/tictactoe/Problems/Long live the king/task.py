x = int(input().strip())
y = int(input().strip())

if x in (1, 8) and y in (1, 8):
    print(3)
elif x in (1, 8) or y in (1, 8):
    print(5)
else:
    print(8)
