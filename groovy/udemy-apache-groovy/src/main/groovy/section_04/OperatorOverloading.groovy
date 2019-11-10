package section_04

class Account {
    String type
    BigDecimal balance = 0

    void deposit(BigDecimal amount) { balance += amount }

    void withdraw(BigDecimal amount) { balance -= amount }

    BigDecimal plus(Account other) { balance + other.balance }
}
