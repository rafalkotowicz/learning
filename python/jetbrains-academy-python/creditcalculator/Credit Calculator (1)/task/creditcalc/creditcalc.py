import math

print('What do you want to calculate?')
print('type "n" - for count of months,')
print('type "a" - for annuity monthly payment,')
print('type "p" - for credit principal:')
action = input()


def count_months():
    print("Enter credit principal:")
    p = int(input())
    print("Enter monthly payment:")
    a = int(input())
    print("Enter credit interest:")
    i = int(input())/12/100

    print()


def count_monthly_payment():
    pass


def count_credit_principal():
    pass


if action == "n":
    count_months()
elif action == "a":
    count_monthly_payment()
elif action == "p":
    count_credit_principal()
else:
    print("Unexpected input")

