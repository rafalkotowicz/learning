import random
import sqlite3
from sqlite3 import Error


class DatabaseConnector:

    def __init__(self, db_path="card.s3db"):
        try:
            self.connection = sqlite3.connect(db_path)
            self.cursor = self.connection.cursor()
        except Error as error:
            print(error)

    def __del__(self):
        self.close_connection()

    def execute_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close_connection(self):
        self.connection.close()

    def init_card_table(self):
        self.execute_query("""
            CREATE TABLE IF NOT EXISTS card (
                id INTEGER PRIMARY KEY,
                number TEXT,
                pin TEXT,
                balance INTEGER DEFAULT 0  
            );
        """)


dc = DatabaseConnector()


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
        user_card = input("Enter your card number:")
        user_pin = input("Enter your PIN:")
        card = find_card_in_db(user_card)
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
        print("2. Add income")
        print("3. Do transfer")
        print("4. Close account")
        print("5. Log out")
        print("0. Exit")
        choice = int(input())

        if 1 == choice:
            print(f'Balance: {card.balance}')
        elif 2 == choice:
            card.add_income(int(input("Enter income:")))
            print("Income was added!")
        elif 3 == choice:
            print("Transfer")
            target_card_number = input("Enter card number:")
            target_card = card.is_card_number_valid(target_card_number)
            if target_card:
                amount_to_transfer = int(input("Enter how much money you want to transfer:"))
                if card.has_enough_money(amount_to_transfer):
                    card.transfer_money(target_card, amount_to_transfer)
                    print("Success!")
                else:
                    print("Not enough money!")

        elif 4 == choice:
            card.close_acount()
            bank_gui()
        elif 5 == choice:
            bank_gui()
        elif 0 == choice:
            print("Bye!")
            exit(0)


class CreditCard:
    IIN = 400000
    all_cards = []

    def __init__(self, *args, **kwargs):
        self.card_number = None
        self.pin = None
        self.balance = 0
        if kwargs.get("is_new", True):
            self.create_new_card()
            self.write_to_db()
            CreditCard.all_cards.append(self)
        else:
            self.load_from_db(kwargs.get("number", None), kwargs.get("pin", None), kwargs.get("balance", 0))
            CreditCard.all_cards.append(self)

    def create_new_card(self):
        self.account_number = random.randint(100000000, 999999999)
        self.card_number_no_luhn = CreditCard.IIN * 10000000000 + self.account_number * 10
        self.luhn = self.calculate_luhn(self.card_number_no_luhn)
        self.card_number = self.card_number_no_luhn + self.luhn
        self.pin = random.randint(1000, 9999)
        print("Your card has been created")
        print("Your card number:")
        print(self.card_number)
        print("Your card PIN:")
        print(self.pin)
        self.balance = 0

    def load_from_db(self, number, pin, balance):
        self.card_number = number
        self.pin = pin
        self.balance = balance

    def __repr__(self):
        return "Card number: " + str(self.card_number) + " PIN: " + str(self.pin)

    def calculate_luhn(self, card_number_no_luhn) -> int:
        card_number_str = str(card_number_no_luhn)
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

    def is_luhn_valid(self, card_number_to_check) -> bool:
        actual_luhn = int(card_number_to_check) % 10
        expected_luhn = self.calculate_luhn(card_number_to_check)
        return actual_luhn == expected_luhn

    def write_to_db(self):
        dc.execute_query(f"""
            INSERT INTO card (number, pin) 
            VALUES ({self.card_number}, {self.pin});
        """)

    def add_income(self, new_balance):
        self.balance += new_balance
        self.update_balance_in_db()

    def update_balance_in_db(self):
        dc.execute_query(f"""
            UPDATE card 
            SET balance = {self.balance} 
            WHERE number = {self.card_number};
        """)

    def is_card_number_valid(self, target_card_number) -> bool:
        if target_card_number == self.card_number:
            print("You can't transfer money to the same account!")
            return False
        if not self.is_luhn_valid(target_card_number):
            print("Probably you made a mistake in the card number. Please try again!")
            return False
        target_card = find_card_in_db(target_card_number)
        if "CardNotFound" == target_card:
            print("Such a card does not exist.")
            return False
        else:
            return target_card

    def has_enough_money(self, amount_to_transfer) -> bool:
        return self.balance >= amount_to_transfer

    def transfer_money(self, target_card, amount_to_transfer) -> None:
        self.balance -= amount_to_transfer
        self.update_balance_in_db()
        target_card.balance += amount_to_transfer
        target_card.update_balance_in_db()

    def close_acount(self) -> None:
        dc.execute_query(f"""
            DELETE FROM card 
            WHERE number = {self.card_number};
        """)


def find_card_in_memory(find_card) -> CreditCard:
    for card in CreditCard.all_cards:
        if card.card_number == find_card:
            return card
    return "CardNotFound"


def find_card_in_db(find_card) -> CreditCard:
    dc.execute_query(f"""
        select number, pin, balance from card where number={find_card};
    """)
    query_result = dc.cursor.fetchone()

    if query_result is not None:
        (number, pin, balance) = query_result
        found_card = CreditCard(is_new=False, number=number, pin=pin, balance=balance)
        return found_card
    else:
        return "CardNotFound"


if __name__ == '__main__':
    dc.init_card_table()
    bank_gui()
