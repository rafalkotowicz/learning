guests = []
while 1:
    guest = input()
    if guest != ".":
        guests.append(guest)
    else:
        break

print(guests)
print(len(guests))
