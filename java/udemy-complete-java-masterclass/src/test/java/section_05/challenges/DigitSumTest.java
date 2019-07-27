package section_05.challenges;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static section_05.challenges.DigitSum.sumDigits;
import static section_05.challenges.DigitSum.sumDigits2;

public class DigitSumTest {
    @Test
    public void sumDigitsNegativeTest() {
        for(int i = -10; i <= 9; i++) {
            assertEquals(-1, sumDigits(i));
        }
    }

    @Test
    public void sumDigitsPositiveTest() {
        assertEquals(2, sumDigits(11));
        assertEquals(1, sumDigits(10));
        assertEquals(6, sumDigits(123));
        assertEquals(45, sumDigits(1234567890));
    }

    @Test
    public void sumDigits2NegativeTest() {
        for(int i = -10; i <= 9; i++) {
            assertEquals(-1, sumDigits2(i));
        }
    }

    @Test
    public void sumDigits2PositiveTest() {
        assertEquals(2, sumDigits2(11));
        assertEquals(1, sumDigits2(10));
        assertEquals(6, sumDigits2(123));
        assertEquals(45, sumDigits2(1234567890));
    }

}
