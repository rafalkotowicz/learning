# Bank
# User Account
# Credit Card
import random


def bank_gui():
    while True:
        print("1. Create an account")
        print("2. Log into account")
        print("0. Exit")
        choice = int(input())

        if choice == 1:
            UserAccount()
        elif choice == 2:
            login_gui()
        elif choice == 0:
            print("Bye!")
            exit(0)
        else:
            print("Invalid option.")


def login_gui():
    while True:
        user_card = int(input("Enter your card number:"))
        user_pin = int(input("Enter your PIN:"))
        user = UserAccount.find_user_by_card_number(user_card)
        if "UserNotFound" == user:
            print("Wrong card number or PIN!")
            bank_gui()
        if user.credit_card.pin == user_pin:
            print("You have successfully logged in!")
            logged_gui(user)
        else:
            print("Wrong card number or PIN!")
            bank_gui()


def logged_gui(user):
    while True:
        print("1. Balance")
        print("2. Log out")
        print("0. Exit")
        choice = int(input())

        if 1 == choice:
            print(f'Balance: {user.balance}')
        elif 2 == choice:
            bank_gui()
        elif 0 == choice:
            print("Bye!")
            exit(0)


class UserAccount:
    all_users = []

    @staticmethod
    def find_user_by_card_number(find_card):
        for user in UserAccount.all_users:
            if user.credit_card.card_number == find_card:
                return user
        return "UserNotFound"

    def __init__(self):
        self.credit_card = CreditCard()
        self.balance = 0
        UserAccount.all_users.append(self)

    def __repr__(self):
        return "Card number: " + str(self.credit_card.card_number) + " PIN: " + str(self.credit_card.pin)


class CreditCard:
    IIN = 400000

    def __init__(self):
        self.account_number = random.randint(100000000, 999999999)
        self.card_number_nocheck = CreditCard.IIN * 10000000000 + self.account_number * 10
        self.luhn = random.randint(0, 9)
        self.card_number = self.card_number_nocheck + self.luhn
        self.pin = random.randint(1000, 9999)
        print("Your card has been created")
        print("Your card number:")
        print(self.card_number)
        print("Your card PIN:")
        print(self.pin)

    def __repr__(self):
        return "Card number: " + str(self.card_number) + " PIN: " + str(self.pin)


bank_gui()
