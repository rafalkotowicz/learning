deposit = int(input().strip())
government_protected_amount = 700_000
interest = 7.1 / 100
how_many_years = 0
while deposit <= government_protected_amount:
    deposit += deposit * interest
    how_many_years += 1
print(how_many_years)
