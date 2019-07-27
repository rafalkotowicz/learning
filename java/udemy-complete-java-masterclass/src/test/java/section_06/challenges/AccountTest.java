package section_06.challenges;

import org.junit.Before;
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.ExpectedException;

import static org.junit.Assert.assertEquals;
import static utils.Constants.TOLERANCE;

public class AccountTest {
    @Rule
    public ExpectedException thrown = ExpectedException.none();
    private Account account;

    @Before
    public void initialTestData() {
        account = new Account("John Wick", "john.wick@o2.pl", "606-060-666");
        assertEquals(0.00, account.getBalance(), TOLERANCE);
    }

    @Test
    public void depositPositiveTest() {
        account.deposit(120.00);
        assertEquals(120.00, account.getBalance(), TOLERANCE);
    }

    @Test
    public void withdrawPositiveTest() {
        account.deposit(120.00);
        assertEquals(120.00, account.getBalance(), TOLERANCE);
        account.witdraw(100.00);
        assertEquals(20.00, account.getBalance(), TOLERANCE);
    }

    @Test
    public void withdrawMoreThanBalanceTest() {
        account.deposit(20.00);
        assertEquals(20.00, account.getBalance(), TOLERANCE);

        thrown.expect(IllegalArgumentException.class);
        thrown.expectMessage("Cannot withdraw more than balance");

        account.witdraw(100.00);
        assertEquals(100.00, account.getBalance(), TOLERANCE);
    }
}
