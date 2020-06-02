prime_numbers = []
for i in range(2, 1000):
    if all([not i % j == 0 for j in range(2, i)]):
        prime_numbers.append(i)
