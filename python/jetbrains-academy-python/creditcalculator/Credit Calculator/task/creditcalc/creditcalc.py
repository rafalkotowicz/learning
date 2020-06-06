import math

print("Enter the credit principal:")
credit_principal = int(input())
print("What do you want to calculate")
print('type "m" - for count of months,')
print('type "p" - for monthly payment:')
action = input()

if action == "m":
    print("Enter monthly payment:")
    payment = int(input())
    months = math.ceil(credit_principal / payment)
    if months == 1:
        print("It takes 1 month to repay the credit")
    else:
        print("It takes", months, "months to repay the credit")

if action == "p":
    print("Enter count of months:")
    months = int(input())
    payment = math.ceil(credit_principal / months)
    last_payment = 0
    if payment * months > credit_principal:
        last_payment = credit_principal - payment * (months - 1)
        print("Your monthly payment =", payment, "with last month payment =", last_payment)
    else:
        print("Your monthly payment =", payment)
