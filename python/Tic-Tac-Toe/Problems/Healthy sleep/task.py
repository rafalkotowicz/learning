# you should sleep >= A
# you should not sleep <= B
# Ann sleeps H hours a day
A = int(input().strip())
B = int(input().strip())
H = int(input().strip())

if A <= H <= B:
    print("Normal")
else:
    if H <= A:
        print("Deficiency")
    else:
        print("Excess")