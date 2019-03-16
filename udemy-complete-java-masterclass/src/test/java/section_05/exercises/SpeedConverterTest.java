package section_05.exercises;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.Assert.assertEquals;
import static section_05.exercises.SpeedConverter.*;

public class SpeedConverterTest {
    private ByteArrayOutputStream caughtOutput = new ByteArrayOutputStream();
    private PrintStream originaOutputStream = System.out;

    @Before
    public void catchOutput() {
        System.setOut(new PrintStream(caughtOutput));
    }

    @After
    public void restoreOutputStream() {
        System.setOut(originaOutputStream);
    }

    @Test
    public void toMilesPerHourInvalidInputTest() {
        assertEquals("Expected invalid input (-1)", -1, toMilesPerHour(-1));
        assertEquals("Expected invalid input (-1)", -1, toMilesPerHour(-113.312));
    }

    @Test
    public void toMilesPerHourPositiveTest() {
        assertEquals(1, toMilesPerHour(1.5));
        assertEquals(6, toMilesPerHour(10.25));
        assertEquals(-1, toMilesPerHour(-5.6));
        assertEquals(16, toMilesPerHour(25.42));
        assertEquals(47, toMilesPerHour(75.114));
    }

    @Test
    public void printConversionInvalidValueTest() {
        printConversion(-1);
        assertEquals("Invalid Value", caughtOutput.toString());
        caughtOutput.reset();
        printConversion(-1.1);
        assertEquals("Invalid Value", caughtOutput.toString());
    }

    @Test
    public void printConversionPositiveTest() {
        printConversion(1.5);
        assertEquals("1.5 km/h = 1 mi/h", caughtOutput.toString());
        caughtOutput.reset();
        printConversion(10.25);
        assertEquals("10.25 km/h = 6 mi/h", caughtOutput.toString());
        caughtOutput.reset();
        printConversion(25.42);
        assertEquals("25.42 km/h = 16 mi/h", caughtOutput.toString());
        caughtOutput.reset();
        printConversion(75.114);
        assertEquals("75.114 km/h = 47 mi/h", caughtOutput.toString());
        caughtOutput.reset();
    }
}
