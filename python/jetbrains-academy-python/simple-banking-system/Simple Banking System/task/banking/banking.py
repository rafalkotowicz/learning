# gui functions
# CreditCard class
import random


def bank_gui():
    while True:
        print("1. Create an account")
        print("2. Log into account")
        print("0. Exit")
        choice = int(input())

        if choice == 1:
            CreditCard()
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
        card = CreditCard.find_card(user_card)
        if "CardNotFound" == card:
            print("Wrong card number or PIN!")
            bank_gui()
        if card.pin == user_pin:
            print("You have successfully logged in!")
            logged_gui(card)
        else:
            print("Wrong card number or PIN!")
            bank_gui()


def logged_gui(card):
    while True:
        print("1. Balance")
        print("2. Log out")
        print("0. Exit")
        choice = int(input())

        if 1 == choice:
            print(f'Balance: {card.balance}')
        elif 2 == choice:
            bank_gui()
        elif 0 == choice:
            print("Bye!")
            exit(0)


class CreditCard:
    IIN = 400000
    all_cards = []

    def __init__(self):
        self.account_number = random.randint(100000000, 999999999)
        self.card_number_no_luhn = CreditCard.IIN * 10000000000 + self.account_number * 10
        self.luhn = self.calculate_luhn()
        self.card_number = self.card_number_no_luhn + self.luhn
        self.pin = random.randint(1000, 9999)
        print("Your card has been created")
        print("Your card number:")
        print(self.card_number)
        print("Your card PIN:")
        print(self.pin)
        self.balance = 0
        CreditCard.all_cards.append(self)

    def __repr__(self):
        return "Card number: " + str(self.card_number) + " PIN: " + str(self.pin)

    def calculate_luhn(self):
        card_number_str = str(self.card_number_no_luhn)
        digit_sum = 0
        for i in range(1, 16):
            current_digit = int(card_number_str[i - 1])
            if i % 2 == 0:
                digit_sum += current_digit
            else:
                digit_sum += current_digit * 2
                if current_digit * 2 > 9:
                    digit_sum -= 9
        return 0 if digit_sum % 10 == 0 else 10 - digit_sum % 10

    @staticmethod
    def find_card(find_card):
        for card in CreditCard.all_cards:
            if card.card_number == find_card:
                return card
        return "CardNotFound"


bank_gui()
