cash = int(input().strip())

chicken_price = 23
goat_price = 678
pig_price = 1296
cow_price = 3848
sheep_price = 6769

if cash < chicken_price:
    print("None")
elif chicken_price <= cash < goat_price:
    amount = cash // chicken_price
    print(amount, "chicken" if amount == 1 else "chickens")
elif goat_price <= cash < pig_price:
    amount = cash // goat_price
    print(amount, "goat" if amount == 1 else "goats")
elif pig_price <= cash < cow_price:
    amount = cash // pig_price
    print(amount, "pig" if amount == 1 else "pigs")
elif cow_price <= cash < sheep_price:
    amount = cash // cow_price
    print(amount, "cow" if amount == 1 else "cows")
elif sheep_price <= cash:
    amount = cash // sheep_price
    print(amount, "sheep" if amount == 1 else "sheep")
