user_input = int(input().strip())

if user_input < 2:
    print("That seems reasonable")
elif user_input < 4:
    print("Do you have time for anything else?")
else:
    print("You need to get outside more!")