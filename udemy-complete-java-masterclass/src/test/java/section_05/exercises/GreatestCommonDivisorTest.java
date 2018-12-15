package section_05.exercises;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static section_05.exercises.GreatestCommonDivisor.getGreatestCommonDivisor;

public class GreatestCommonDivisorTest {
    @Test
    public void getGreatestCommonDivisorInvalidInputTest() {
        assertEquals(-1, getGreatestCommonDivisor(1, 1));
        assertEquals(-1, getGreatestCommonDivisor(1, 10));
        assertEquals(-1, getGreatestCommonDivisor(10, 9));
    }

    @Test
    public void getGreatestCommonDivisorTest() {
        assertEquals(5, getGreatestCommonDivisor(25, 15));
        assertEquals(6, getGreatestCommonDivisor(12, 30));
        assertEquals(9, getGreatestCommonDivisor(81, 153));
    }

}
