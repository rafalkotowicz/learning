from math import log, ceil


def months_to_years(months):
    years = months // 12
    months = months % 12
    return years, months


def count_periods(i, a, p):
    # print("Enter credit principal:")
    # p = int(input())
    # print("Enter monthly payment:")
    # a = int(input())
    # print("Enter credit interest:")
    # i = float(input()) / 12 / 100

    months = ceil(log((a / (a - i * p)), 1 + i))
    years, months = months_to_years(months)
    if years > 0:
        if years == 1:
            message_years = "You need 1 year"
        else:
            message_years = f"You need {years} years"
    else:
        message_years = ""
    if months > 0:
        if years == 1:
            message_months = " and 1 month"
        else:
            message_months = f" and {months} months"
    else:
        message_months = ""
    print(f"{message_years}{message_months} to repay this credit!")


#
#
# def count_monthly_payment():
#     print("Enter credit principal:")
#     p = int(input())
#     print("Enter count of periods:")
#     n = int(input())
#     print("Enter credit interest:")
#     i = float(input()) / 12 / 100
#
#     annuity_payment = ceil(p * ((i * pow(1 + i, n)) / (pow(1 + i, n) - 1)))
#     print(f"Your annuity payment = {annuity_payment}!")
#
#
# def count_credit_principal():
#     print("Enter monthly payment:")
#     a = float(input())
#     print("Enter count of periods:")
#     n = int(input())
#     print("Enter credit interest:")
#     i = float(input()) / 12 / 100
#
#     principal = floor(a / ((i * pow(1 + i, n)) / (pow(1 + i, n) - 1)))
#     print(f"Your credit principal = {principal}!")
#
#
# print('What do you want to calculate?')
# print('type "n" - for count of months,')
# print('type "a" - for annuity monthly payment,')
# print('type "p" - for credit principal:')
# action = input()
# if action == "n":
#     count_periods()
# elif action == "a":
#     count_monthly_payment()
# elif action == "p":
#     count_credit_principal()
# else:
#     print("Unexpected input")

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type", required=True, choices=["annuity", "diff"])
parser.add_argument("--interest", required=True, type=float, help="Credit interest. Specify without percent sign.")
parser.add_argument("--payment", type=float, help="Monthly payment.")
parser.add_argument("--principal", type=float, help="Value of entire borrowed sum.")
parser.add_argument("--periods", type=int, help="Denotes the number of months needed to repay the credit. If missing,"
                                                " it will be calculated based on the interest, annuity payments and "
                                                "principal.")
args = parser.parse_args()

import sys


def validate_parameter(param):
    if param is not None:
        if param < 0:
            print("Incorrect parameters")
            sys.exit()


if len(sys.argv) < 5:
    print("Incorrect parameters")
    sys.exit()

interest = args.interest / 12 / 100
validate_parameter(interest)
payment = args.payment
validate_parameter(payment)
principal = args.principal
validate_parameter(principal)
periods = args.periods
validate_parameter(periods)

# if args.payment == "annuity" and interest is not None and payment is not None and principal is not None:
count_periods(interest, payment, principal)

print(f'Type: {args.type}')
print(f'Interest: {args.interest}')
print(f'Payment: {args.payment}')
print(f'Principal: {args.principal}')
print(f'Periods: {args.periods}')
