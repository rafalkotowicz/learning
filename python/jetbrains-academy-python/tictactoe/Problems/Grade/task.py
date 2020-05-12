score = int(input().strip())
maximum = int(input().strip())
percentage = score / maximum * 100

if percentage >= 90:
    print("A")
elif 80 <= percentage < 90:
    print("B")
elif 70 <= percentage < 80:
    print("C")
elif 60 <= percentage < 70:
    print("D")
else:
    print("F")