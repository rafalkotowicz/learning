package section_05.exercises;

import org.junit.Assert;
import org.junit.Test;

import static section_05.exercises.EvenDigitSum.*;

public class EvenDigitSumTest {
    @Test
    public void getEventDigitSumNegativeTest () {
        Assert.assertEquals(-1, getEvenDigitSum(-1));
        Assert.assertEquals(-1, getEvenDigitSum(-1123));
    }

    @Test
    public void getEventDigitSumPositiveTest () {
        Assert.assertEquals(20, getEvenDigitSum(1234567890));
        Assert.assertEquals(4, getEvenDigitSum(252));
    }
}
