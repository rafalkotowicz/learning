package section_04

class Account {
    String type
    BigDecimal balance = 0

    void deposit(BigDecimal amount) { balance += amount }

    void withdraw(BigDecimal amount) { balance -= amount }

    BigDecimal plus(Account other) { balance + other.balance }
}

Account checking = new Account(type: "Checking")
checking.deposit(100.00)
Account savings = new Account(type: "Savings")
savings.deposit(50.00)

BigDecimal total = checking + savings
println "Result is: $total"