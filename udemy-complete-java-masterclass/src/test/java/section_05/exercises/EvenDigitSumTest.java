package section_05.exercises;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static section_05.exercises.EvenDigitSum.getEvenDigitSum;

public class EvenDigitSumTest {
    @Test
    public void getEventDigitSumNegativeTest () {
        assertEquals(-1, getEvenDigitSum(-1));
        assertEquals(-1, getEvenDigitSum(-1123));
    }

    @Test
    public void getEventDigitSumPositiveTest () {
        assertEquals(20, getEvenDigitSum(1234567890));
        assertEquals(4, getEvenDigitSum(252));
    }
}
