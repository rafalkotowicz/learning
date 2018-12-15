package section_05.exercises;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static section_05.exercises.FirstLastDigitSum.sumFirstAndLastDigit;

public class FirstLastDigitSumTest {
    @Test
    public void sumFirstAndLastDigitNegativeTest() {
        assertEquals(-1, sumFirstAndLastDigit(-1));
        assertEquals(-1, sumFirstAndLastDigit(-123));
    }

    @Test
    public void sumFirstAndLastDigitPositiveTest() {
        assertEquals(4, sumFirstAndLastDigit(1000000003));
        assertEquals(2, sumFirstAndLastDigit(1));
        assertEquals(4, sumFirstAndLastDigit(252));
        assertEquals(9, sumFirstAndLastDigit(257));
        assertEquals(0, sumFirstAndLastDigit(0));
        assertEquals(10, sumFirstAndLastDigit(5));
    }


}
