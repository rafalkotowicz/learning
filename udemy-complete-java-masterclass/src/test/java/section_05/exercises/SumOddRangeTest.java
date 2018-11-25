package section_05.exercises;

import org.junit.Test;

import static org.junit.Assert.*;
import static section_05.exercises.SumOddRange.*;

public class SumOddRangeTest {
    @Test
    public void isOddTest() {
        assertFalse(isOdd(0));
        assertFalse(isOdd(-1));

        assertTrue(isOdd(1));
        assertTrue(isOdd(2_000_000_001));

        assertFalse(isOdd(2));
        assertFalse(isOdd(2_000_000_000));
    }

    @Test
    public void sumOddParameterTest() {
        assertEquals(-1, sumOdd(0, 0));
        assertEquals(-1, sumOdd(-1, 1));
        assertEquals(-1, sumOdd(1, -1));
        assertEquals(-1, sumOdd(100, 1));
    }

    @Test
    public void sumOddReturnedValueTest() {
        assertEquals(2500, sumOdd(1, 100));
        assertEquals(0, sumOdd(100, 100));
        assertEquals(247500, sumOdd(100, 1000));
    }
}