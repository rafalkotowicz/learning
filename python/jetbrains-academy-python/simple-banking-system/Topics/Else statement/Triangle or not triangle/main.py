angle_1 = int(input())
angle_2 = int(input())
angle_3 = int(input())

TRIANGLE_ANGLES_CONST = 180
if angle_1 + angle_2 + angle_3 == TRIANGLE_ANGLES_CONST:
    print("The triangle is valid!")
else:
    print("The triangle is not valid!")
