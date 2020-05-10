# Save the input in this variable
ticket = int(input())

# Add up the digits for each half
half1 = ticket // 1000 % 10 + ticket // 1000 // 10 % 10 + ticket // 1000 // 100
half2 = ticket % 1000 % 10 + ticket % 1000 // 10 % 10 + ticket % 1000 // 100

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")
