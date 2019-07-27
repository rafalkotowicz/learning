package section_04.exercises;

import org.junit.Test;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import static section_04.exercises.LeapYear.isLeapYear;

public class LeapYearTest {
    @Test
    public void isLeapYearTest() {
        assertFalse(isLeapYear(-1600));
        assertTrue(isLeapYear(1600));
        assertFalse(isLeapYear(2017));
        assertTrue(isLeapYear(2000));
        assertFalse(isLeapYear(100));
        assertFalse(isLeapYear(200));
        assertFalse(isLeapYear(300));
    }
}
