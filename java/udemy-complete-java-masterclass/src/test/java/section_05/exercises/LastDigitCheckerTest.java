package section_05.exercises;

import org.junit.Test;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import static section_05.exercises.LastDigitChecker.hasSameLastDigit;

public class LastDigitCheckerTest {
    @Test
    public void hasSameLastDigitInputValidityTest() {
        assertFalse(hasSameLastDigit(123,124,-1));
        assertFalse(hasSameLastDigit(123,-1,1));
        assertFalse(hasSameLastDigit(-1,1,1));
    }
    @Test
    public void hasSameLastDigitTest() {
        assertFalse(hasSameLastDigit(23,24,25));
        assertFalse(hasSameLastDigit(23,32,41));

        assertTrue(hasSameLastDigit(41,22,71));
        assertTrue(hasSameLastDigit(23,31,41));
        assertTrue(hasSameLastDigit(23,33,41));
    }
}
