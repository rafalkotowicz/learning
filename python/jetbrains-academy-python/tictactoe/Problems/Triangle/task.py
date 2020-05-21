height = int(input())
for i in range(0, height):
    print(" " * (height - i - 1), end="")
    print("#" * (2 * i + 1))
