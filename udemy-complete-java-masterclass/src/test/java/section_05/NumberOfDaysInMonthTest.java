package section_05;

import org.junit.Assert;
import org.junit.Test;
import section_05.exercises.NumberOfDaysInMonth;

public class NumberOfDaysInMonthTest {
    @Test
    public void isLeapYearTest() {
        Assert.assertTrue(NumberOfDaysInMonth.isLeapYear(2000));
        Assert.assertTrue(NumberOfDaysInMonth.isLeapYear(2004));
        Assert.assertTrue(NumberOfDaysInMonth.isLeapYear(2008));
        Assert.assertTrue(NumberOfDaysInMonth.isLeapYear(2012));
        Assert.assertTrue(NumberOfDaysInMonth.isLeapYear(2016));
        Assert.assertTrue(NumberOfDaysInMonth.isLeapYear(2020));
        Assert.assertTrue(NumberOfDaysInMonth.isLeapYear(4));

        Assert.assertFalse(NumberOfDaysInMonth.isLeapYear(100));
        Assert.assertFalse(NumberOfDaysInMonth.isLeapYear(200));
        Assert.assertFalse(NumberOfDaysInMonth.isLeapYear(300));
        Assert.assertFalse(NumberOfDaysInMonth.isLeapYear(500));
        Assert.assertFalse(NumberOfDaysInMonth.isLeapYear(600));
        Assert.assertFalse(NumberOfDaysInMonth.isLeapYear(700));
        Assert.assertFalse(NumberOfDaysInMonth.isLeapYear(900));

        Assert.assertFalse(NumberOfDaysInMonth.isLeapYear(0));
        Assert.assertFalse(NumberOfDaysInMonth.isLeapYear(10_000));
        Assert.assertFalse(NumberOfDaysInMonth.isLeapYear(-1));
    }

    @Test
    public void getDaysInMonthTest() {
        int i = 0;
        Assert.assertEquals(31, NumberOfDaysInMonth.getDaysInMonth(1,2000));
        Assert.assertEquals(29, NumberOfDaysInMonth.getDaysInMonth(2,2000));
        Assert.assertEquals(28, NumberOfDaysInMonth.getDaysInMonth(2,2001));
        Assert.assertEquals(31, NumberOfDaysInMonth.getDaysInMonth(3,2001));
        Assert.assertEquals(30, NumberOfDaysInMonth.getDaysInMonth(4,2001));
        Assert.assertEquals(31, NumberOfDaysInMonth.getDaysInMonth(5,2001));
        Assert.assertEquals(30, NumberOfDaysInMonth.getDaysInMonth(6,2001));
        Assert.assertEquals(31, NumberOfDaysInMonth.getDaysInMonth(7,2001));
        Assert.assertEquals(31, NumberOfDaysInMonth.getDaysInMonth(8,2001));
        Assert.assertEquals(30, NumberOfDaysInMonth.getDaysInMonth(9,2001));
        Assert.assertEquals(31, NumberOfDaysInMonth.getDaysInMonth(10,2001));
        Assert.assertEquals(30, NumberOfDaysInMonth.getDaysInMonth(11,2001));
        Assert.assertEquals(31, NumberOfDaysInMonth.getDaysInMonth(12,2001));
    }
}
