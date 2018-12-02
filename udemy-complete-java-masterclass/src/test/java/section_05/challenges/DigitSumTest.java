package section_05.challenges;

import org.junit.Assert;
import org.junit.Test;

public class DigitSumTest {
    @Test
    public void sumDigitsNegativeTest() {
        for(int i = -10; i <= 9; i++) {
            Assert.assertEquals(-1, DigitSum.sumDigits(i));
        }
    }

    @Test
    public void sumDigitsPositiveTest() {
        Assert.assertEquals(2, DigitSum.sumDigits(11));
        Assert.assertEquals(1, DigitSum.sumDigits(10));
        Assert.assertEquals(6, DigitSum.sumDigits(123));
        Assert.assertEquals(45, DigitSum.sumDigits(1234567890));
    }

    @Test
    public void sumDigits2NegativeTest() {
        for(int i = -10; i <= 9; i++) {
            Assert.assertEquals(-1, DigitSum.sumDigits2(i));
        }
    }

    @Test
    public void sumDigits2PositiveTest() {
        Assert.assertEquals(2, DigitSum.sumDigits2(11));
        Assert.assertEquals(1, DigitSum.sumDigits2(10));
        Assert.assertEquals(6, DigitSum.sumDigits2(123));
        Assert.assertEquals(45, DigitSum.sumDigits2(1234567890));
    }

}
