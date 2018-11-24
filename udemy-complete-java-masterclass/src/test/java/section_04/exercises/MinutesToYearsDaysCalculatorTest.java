package section_04.exercises;

import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static section_04.exercises.MinutesToYearsDaysCalculator.printYearsAndDays;

public class MinutesToYearsDaysCalculatorTest {
    private final ByteArrayOutputStream caughtOutput = new ByteArrayOutputStream();
    private final PrintStream originalOut = System.out;

    @Before
    public void setUpStream() {
        System.setOut(new PrintStream(caughtOutput));
    }

    @After
    public void restoreStream() {
        System.setOut(originalOut);
    }

    @Test
    public void printYearsAndDaysTest() {
        caughtOutput.reset();
        printYearsAndDays(525600);
        Assert.assertEquals("525600 min = 1 y and 0 d", caughtOutput.toString());
        caughtOutput.reset();
        printYearsAndDays(1051200);
        Assert.assertEquals("1051200 min = 2 y and 0 d", caughtOutput.toString());
        caughtOutput.reset();
        printYearsAndDays(561600);
        Assert.assertEquals("561600 min = 1 y and 25 d", caughtOutput.toString());
        caughtOutput.reset();
        printYearsAndDays(-1123);
        Assert.assertEquals("Invalid Value", caughtOutput.toString());
        caughtOutput.reset();
        printYearsAndDays(-525600   );
        Assert.assertEquals("Invalid Value", caughtOutput.toString());
        caughtOutput.reset();
    }
}
