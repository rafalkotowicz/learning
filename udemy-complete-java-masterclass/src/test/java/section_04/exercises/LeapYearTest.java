package section_04.exercises;

import org.junit.Assert;
import org.junit.Test;

import static section_04.exercises.LeapYear.isLeapYear;

public class LeapYearTest {
    @Test
    public void isLeapYearTest() {
        Assert.assertFalse(isLeapYear(-1600));
        Assert.assertTrue(isLeapYear(1600));
        Assert.assertFalse(isLeapYear(2017));
        Assert.assertTrue(isLeapYear(2000));
        Assert.assertFalse(isLeapYear(100));
        Assert.assertFalse(isLeapYear(200));
        Assert.assertFalse(isLeapYear(300));
    }
}
