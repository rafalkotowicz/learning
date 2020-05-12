x = float(input().strip())
y = float(input().strip())

if x > 0:
    if y > 0:
        print("I")
    else:
        print("IV")
else:
    if y > 0:
        print("II")
    else:
        print("III")