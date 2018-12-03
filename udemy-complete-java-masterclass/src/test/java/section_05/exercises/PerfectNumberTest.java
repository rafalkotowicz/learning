package section_05.exercises;

import org.junit.Assert;
import org.junit.Test;

import static section_05.exercises.PerfectNumber.isPerfectNumber;

public class PerfectNumberTest {
    @Test
    public void isPerfectNumberInvalidInputTest() {
        Assert.assertFalse(isPerfectNumber(0));
        Assert.assertFalse(isPerfectNumber(-1));
        Assert.assertFalse(isPerfectNumber(-1231231));
    }

    @Test
    public void isPerfectNumberPositiveTest() {
        Assert.assertTrue(isPerfectNumber(28));
        Assert.assertTrue(isPerfectNumber(6));
    }

    @Test
    public void isPerfectNumberNegativeTest() {
        Assert.assertFalse(isPerfectNumber(5));
        Assert.assertFalse(isPerfectNumber(10001));
    }


}
