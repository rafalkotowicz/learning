package section_04.exercises;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static java.lang.System.setOut;
import static org.junit.Assert.assertEquals;
import static section_04.exercises.IntEqualityPrinter.printEqual;

public class IntEqualityPrinterTest {
    private final ByteArrayOutputStream caughtOutput = new ByteArrayOutputStream();
    private final PrintStream originalOutputStream = System.out;

    @Before
    public void setUpOutputStream() {
        setOut(new PrintStream(caughtOutput));
    }

    @After
    public void restoreOutputStream() {
        setOut(originalOutputStream);
    }

    @Test
    public void printEqualTest() {
        assertPrintout(-1, 1, 1, "Invalid Value");
        assertPrintout(1, -1, 1, "Invalid Value");
        assertPrintout(1, 1, -1, "Invalid Value");
        assertPrintout(1, 1, 1, "All numbers are equal");
        assertPrintout(1, 2, 3, "All numbers are different");
        assertPrintout(1, 1, 3, "Neither all are equal or different");
    }

    private void assertPrintout(int i, int i2, int i3, String s) {
        printEqual(i, i2, i3);
        assertEquals(s, caughtOutput.toString().trim());
        caughtOutput.reset();
    }
}
