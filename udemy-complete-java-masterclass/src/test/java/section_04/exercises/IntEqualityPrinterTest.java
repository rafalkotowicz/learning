package section_04.exercises;

import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

public class IntEqualityPrinterTest {
    private final ByteArrayOutputStream caughtOutput = new ByteArrayOutputStream();
    private final PrintStream originalOutputStream = System.out;

    @Before
    public void setUpOutputStream() {
        System.setOut(new PrintStream(caughtOutput));
    }

    @After
    public void restoreOutputStream() {
        System.setOut(originalOutputStream);
    }

    @Test
    public void printEqualTest() {
        IntEqualityPrinter.printEqual(-1, 1, 1);
        Assert.assertEquals("Invalid Value", caughtOutput.toString().trim());
        caughtOutput.reset();
        IntEqualityPrinter.printEqual(1, -1, 1);
        Assert.assertEquals("Invalid Value", caughtOutput.toString().trim());
        caughtOutput.reset();
        IntEqualityPrinter.printEqual(1, 1, -1);
        Assert.assertEquals("Invalid Value", caughtOutput.toString().trim());
        caughtOutput.reset();
        IntEqualityPrinter.printEqual(1, 1, 1);
        Assert.assertEquals("All numbers are equal", caughtOutput.toString().trim());
        caughtOutput.reset();
        IntEqualityPrinter.printEqual(1, 2, 3);
        Assert.assertEquals("All numbers are different", caughtOutput.toString().trim());
        caughtOutput.reset();
        IntEqualityPrinter.printEqual(1, 1, 3);
        Assert.assertEquals("Neither all are equal or different", caughtOutput.toString().trim());
        caughtOutput.reset();
    }
}
