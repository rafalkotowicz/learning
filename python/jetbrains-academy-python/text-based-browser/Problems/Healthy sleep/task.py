a = int(input())
b = int(input())
h = int(input())

if h < a:
    print("Deficiency")

if h > b:
    print("Excess")

if a <= h <= b:
    print("Normal")
