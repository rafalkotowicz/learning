"""Bank account implementation for the Exercism bank-account exercise."""


class BankAccount:
    """Represents a simple open/close bank account with integer balance."""

    def __init__(self):
        """Create a closed account with zero balance."""
        self._is_open = False
        self._balance = 0

    def _ensure_open(self):
        """Raise an error when an operation is executed on a closed account."""
        if not self._is_open:
            raise ValueError("account not open")

    def get_balance(self):
        """Return current balance for an open account."""
        self._ensure_open()
        return self._balance

    def open(self):
        """Open account and reset balance to zero."""
        if self._is_open:
            raise ValueError("account already open")
        self._is_open = True
        self._balance = 0

    def deposit(self, amount):
        """Add a positive amount to balance."""
        self._ensure_open()
        if amount <= 0:
            raise ValueError("amount must be greater than 0")
        self._balance += amount

    def withdraw(self, amount):
        """Subtract a positive amount that does not exceed balance."""
        self._ensure_open()
        if amount <= 0:
            raise ValueError("amount must be greater than 0")
        if amount > self._balance:
            raise ValueError("amount must be less than balance")
        self._balance -= amount

    def close(self):
        """Close account and clear balance."""
        self._ensure_open()
        self._is_open = False
        self._balance = 0
