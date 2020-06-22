import argparse

import sys
from math import log, ceil, floor


def months_to_years(months):
    years = months // 12
    months = months % 12
    return years, months


def count_overpayment(periods, payment, principal):
    print("Overpayment = {overpayment}".format(overpayment=int(periods * payment - principal)))


def count_periods(interest, payment, principal):
    months_to_pay = ceil(log((payment / (payment - interest * principal)), 1 + interest))
    years, months_to_print = months_to_years(months_to_pay)
    if years > 0:
        if years == 1:
            message_years = "You need 1 year"
        else:
            message_years = f"You need {years} years"
    else:
        message_years = ""
    if months_to_print > 0:
        if years == 1:
            message_months = " and 1 month"
        else:
            message_months = f" and {months_to_print} months"
    else:
        message_months = ""
    print(f"{message_years}{message_months} to repay this credit!")
    count_overpayment(months_to_pay, payment, principal)


def count_monthly_payment(principal, periods, interest):
    annuity_payment = ceil(principal * ((interest * pow(1 + interest, periods)) / (pow(1 + interest, periods) - 1)))
    print(f"Your annuity payment = {annuity_payment}!")
    count_overpayment(periods, annuity_payment, principal)


def count_credit_principal(payment, periods, interest):
    principal = floor(payment / ((interest * pow(1 + interest, periods)) / (pow(1 + interest, periods) - 1)))
    print(f"Your credit principal = {principal}!")
    count_overpayment(periods, payment, principal)


def count_differentiate_payment(principal, periods, interest):
    paid_back = 0
    differentiate_payment = []
    for m in range(1, periods + 1):
        differentiate_payment.append(
            ceil(principal / periods + interest * (principal - ((principal * (m - 1)) / periods))))
        print(f"Month {m}: paid out {differentiate_payment[m - 1]}")
    print("Overpayment = {}".format(ceil(sum(differentiate_payment)) - int(principal)))


if len(sys.argv) < 5:
    print("Incorrect parameters")
    sys.exit()

parser = argparse.ArgumentParser()
parser.add_argument("--type", required=True, choices=["annuity", "diff"])
parser.add_argument("--interest", type=float, help="Credit interest. Specify without percent sign.")
parser.add_argument("--payment", type=float, help="Monthly payment.")
parser.add_argument("--principal", type=float, help="Value of entire borrowed sum.")
parser.add_argument("--periods", type=int, help="Denotes the number of months needed to repay the credit. If missing,"
                                                " it will be calculated based on the interest, annuity payments and "
                                                "principal.")
args = parser.parse_args()

if args.interest is None:
    print("Incorrect parameters")
    sys.exit()


def validate_parameter(param):
    if param is not None:
        if param < 0:
            print("Incorrect parameters")
            sys.exit()
    return param


interest = validate_parameter(args.interest) / 12 / 100
payment = validate_parameter(args.payment)
principal = validate_parameter(args.principal)
periods = validate_parameter(args.periods)

if args.type == "annuity" and periods is None and interest is not None and payment is not None and principal is not None:
    count_periods(interest, payment, principal)

if args.type == "annuity" and payment is None and interest is not None and periods is not None and principal is not None:
    count_monthly_payment(principal, periods, interest)

if args.type == "annuity" and principal is None and interest is not None and periods is not None and payment is not None:
    count_credit_principal(payment, periods, interest)

if args.type == "diff" and payment is None and principal is not None and interest is not None and periods is not None:
    count_differentiate_payment(principal, periods, interest)
