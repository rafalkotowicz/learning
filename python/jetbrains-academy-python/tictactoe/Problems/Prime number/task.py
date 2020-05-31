number = int(input().strip())
is_prime = True

if number == 1:
    is_prime = False
if number == 2:
    is_prime = True

i = 3
while i <= number ** 1 / 2:
    if number % i == 0:
        is_prime = False
        break
    i += 1

if is_prime:
    print("This number is prime")
else:
    print("This number is not prime")
