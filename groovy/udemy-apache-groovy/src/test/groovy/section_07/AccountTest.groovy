package section_07

import org.junit.Rule
import org.junit.Test
import org.junit.rules.ExpectedException

import java.security.InvalidParameterException

class AccountTest {
    @Rule
    public ExpectedException expectedException = ExpectedException.none()

    @Test
    void exceptionThrownWhenDepositNotPositiveTest() {
        expectedException.expect(InvalidParameterException)
        expectedException.expectMessage("Cannot deposit 0 or less")
        Account account = new Account()
        account.deposit(0 as BigDecimal)
    }

    @Test
    void processBulkDepositsPositiveTest() {
        Account account = new Account()
        account.deposit([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])
        assert 55 == account.balance
    }

}
