import sys

n = int(input())
denominator = int(input())
if denominator == 0:
    print("Division by zero is not supported")
    sys.exit()

print(n // denominator)
