package section_04.exercises;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static java.lang.System.setOut;
import static org.junit.Assert.assertEquals;
import static section_04.exercises.MinutesToYearsDaysCalculator.printYearsAndDays;

public class MinutesToYearsDaysCalculatorTest {
    private final ByteArrayOutputStream caughtOutput = new ByteArrayOutputStream();
    private final PrintStream originalOut = System.out;

    @Before
    public void setUpStream() {
        setOut(new PrintStream(caughtOutput));
    }

    @After
    public void restoreStream() {
        setOut(originalOut);
    }

    @Test
    public void printYearsAndDaysTest() {
        caughtOutput.reset();
        printYearsAndDays(525600);
        assertEquals("525600 min = 1 y and 0 d", caughtOutput.toString());
        caughtOutput.reset();
        printYearsAndDays(1051200);
        assertEquals("1051200 min = 2 y and 0 d", caughtOutput.toString());
        caughtOutput.reset();
        printYearsAndDays(561600);
        assertEquals("561600 min = 1 y and 25 d", caughtOutput.toString());
        caughtOutput.reset();
        printYearsAndDays(-1123);
        assertEquals("Invalid Value", caughtOutput.toString());
        caughtOutput.reset();
        printYearsAndDays(-525600   );
        assertEquals("Invalid Value", caughtOutput.toString());
        caughtOutput.reset();
    }
}
