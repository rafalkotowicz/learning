class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        new_cents = self.cents + deposit_cents
        self.dollars += deposit_dollars + int(new_cents / 100)
        self.cents = new_cents % 100
