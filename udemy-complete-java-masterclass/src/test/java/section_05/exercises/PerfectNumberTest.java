package section_05.exercises;

import org.junit.Test;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import static section_05.exercises.PerfectNumber.isPerfectNumber;

public class PerfectNumberTest {
    @Test
    public void isPerfectNumberInvalidInputTest() {
        assertFalse(isPerfectNumber(0));
        assertFalse(isPerfectNumber(-1));
        assertFalse(isPerfectNumber(-1231231));
    }

    @Test
    public void isPerfectNumberPositiveTest() {
        assertTrue(isPerfectNumber(28));
        assertTrue(isPerfectNumber(6));
    }

    @Test
    public void isPerfectNumberNegativeTest() {
        assertFalse(isPerfectNumber(5));
        assertFalse(isPerfectNumber(10001));
    }


}
