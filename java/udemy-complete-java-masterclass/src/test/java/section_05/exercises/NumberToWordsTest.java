package section_05.exercises;

import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static java.lang.System.setOut;
import static org.junit.Assert.assertEquals;
import static section_05.exercises.NumberToWords.*;

public class NumberToWordsTest {
    private final ByteArrayOutputStream caughtOutput = new ByteArrayOutputStream();
    private PrintStream originalOutputStream = System.out;

    @Test public void getDigitCountInvalidInputTest() {
        assertEquals(-1, getDigitCount(-1));
        assertEquals(-1, getDigitCount(-1123));
        assertEquals(-1, getDigitCount(-13));
    }
    @Test public void getDigitCountPositiveTest() {
        assertEquals(1, getDigitCount(0));
        assertEquals(1, getDigitCount(3));
        assertEquals(2, getDigitCount(10));
        assertEquals(10, getDigitCount(1021231233));
    }
    @Test public void reversePositiveTest() {
        assertEquals(121, reverse(121));
        assertEquals(1, reverse(100));
        assertEquals(321, reverse(123));
        assertEquals(1234, reverse(4321));
        assertEquals(3210123, reverse(3210123));
        assertEquals(123456789, reverse(987654321));
        assertEquals(-12345, reverse(-54321));
    }
    @Test public void numberToWordsInvalidParameterTest() {
        assertTwoWordsTest(-1, "Invalid Value ");
        assertTwoWordsTest(-123123, "Invalid Value ");
    }
    @Test public void numberToWordsPositiveTest() {
        assertTwoWordsTest(123, "One Two Three ");
        assertTwoWordsTest(1010, "One Zero One Zero ");
        assertTwoWordsTest(1000, "One Zero Zero Zero ");
    }

    private void assertTwoWordsTest(int number, String expectedOutput) {
        catchStandardOutput();
        numberToWords(number);
        assertEquals(expectedOutput, caughtOutput.toString());
        caughtOutput.reset();
        restoreStandardOutput();
    }
    private void catchStandardOutput() {
        setOut(new PrintStream(caughtOutput));
    }
    private void restoreStandardOutput() {
        setOut(originalOutputStream);
    }


}
