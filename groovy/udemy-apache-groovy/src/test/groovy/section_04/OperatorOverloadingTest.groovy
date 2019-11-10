package section_04

import org.junit.Test

class OperatorOverloadingTest {
    @Test
    public void addingBalanceOfTwoAccountsTest() {
        Account checking = new Account(type: "Checking")
        checking.deposit(100.00)
        Account savings = new Account(type: "Savings")
        savings.deposit(50.00)
        BigDecimal total = checking + savings
        assert 150 == total
    }
}
