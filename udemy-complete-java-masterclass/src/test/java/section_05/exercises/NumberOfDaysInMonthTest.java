package section_05.exercises;

import org.junit.Test;

import static org.junit.Assert.*;
import static section_05.exercises.NumberOfDaysInMonth.getDaysInMonth;
import static section_05.exercises.NumberOfDaysInMonth.isLeapYear;

public class NumberOfDaysInMonthTest {
    @Test
    public void isLeapYearTest() {
        assertTrue(isLeapYear(2000));
        assertTrue(isLeapYear(2004));
        assertTrue(isLeapYear(2008));
        assertTrue(isLeapYear(2012));
        assertTrue(isLeapYear(2016));
        assertTrue(isLeapYear(2020));
        assertTrue(isLeapYear(4));

        assertFalse(isLeapYear(100));
        assertFalse(isLeapYear(200));
        assertFalse(isLeapYear(300));
        assertFalse(isLeapYear(500));
        assertFalse(isLeapYear(600));
        assertFalse(isLeapYear(700));
        assertFalse(isLeapYear(900));

        assertFalse(isLeapYear(0));
        assertFalse(isLeapYear(10_000));
        assertFalse(isLeapYear(-1));
    }

    @Test
    public void getDaysInMonthTest() {
        int i = 0;
        assertEquals(31, getDaysInMonth(1,2000));
        assertEquals(29, getDaysInMonth(2,2000));
        assertEquals(28, getDaysInMonth(2,2001));
        assertEquals(31, getDaysInMonth(3,2001));
        assertEquals(30, getDaysInMonth(4,2001));
        assertEquals(31, getDaysInMonth(5,2001));
        assertEquals(30, getDaysInMonth(6,2001));
        assertEquals(31, getDaysInMonth(7,2001));
        assertEquals(31, getDaysInMonth(8,2001));
        assertEquals(30, getDaysInMonth(9,2001));
        assertEquals(31, getDaysInMonth(10,2001));
        assertEquals(30, getDaysInMonth(11,2001));
        assertEquals(31, getDaysInMonth(12,2001));
    }
}
