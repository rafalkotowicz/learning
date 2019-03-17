package section_06.challenges;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.ExpectedException;

public class BankAccountTest {
    private BankAccount bankAccount;
    private double TOLERANCE = 0.00000001;

    @Rule
    public ExpectedException thrown = ExpectedException.none();

    @Before
    public void initialTestData() {
        bankAccount = new BankAccount("John Wick", "john.wick@o2.pl", "606-060-666");
        Assert.assertEquals(0.00, bankAccount.getBalance(), TOLERANCE);
    }

    @Test
    public void depositPositiveTest() {
        bankAccount.deposit(120.00);
        Assert.assertEquals(120.00, bankAccount.getBalance(), TOLERANCE);
    }

    @Test
    public void withdrawPositiveTest() {
        bankAccount.deposit(120.00);
        Assert.assertEquals(120.00, bankAccount.getBalance(), TOLERANCE);
        bankAccount.witdraw(100.00);
        Assert.assertEquals(20.00, bankAccount.getBalance(), TOLERANCE);
    }

    @Test
    public void withdrawMoreThanBalanceTest() {
        bankAccount.deposit(20.00);
        Assert.assertEquals(20.00, bankAccount.getBalance(), TOLERANCE);

        thrown.expect(IllegalArgumentException.class);
        thrown.expectMessage("Cannot withdraw more than balance");

        bankAccount.witdraw(100.00);
        Assert.assertEquals(100.00, bankAccount.getBalance(), TOLERANCE);
    }


}
