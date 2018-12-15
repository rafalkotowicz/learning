package section_05.exercises;

import org.junit.Test;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import static section_05.exercises.SharedDigit.hasSharedDigit;

public class SharedDigitTest {
    @Test
    public void hasShareDigitTest() {
        assertFalse(hasSharedDigit(9, 99));
        assertFalse(hasSharedDigit(11, 100));
        assertFalse(hasSharedDigit(1, 1));
        assertFalse(hasSharedDigit(1, 100));
        assertTrue(hasSharedDigit(12, 23));
        assertTrue(hasSharedDigit(15, 55));
        assertTrue(hasSharedDigit(12, 13));
    }
}
