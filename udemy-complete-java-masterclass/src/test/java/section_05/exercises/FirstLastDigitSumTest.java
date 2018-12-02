package section_05.exercises;

import org.junit.Assert;
import org.junit.Test;

import static section_05.exercises.FirstLastDigitSum.*;

public class FirstLastDigitSumTest {
    @Test
    public void sumFirstAndLastDigitNegativeTest() {
        Assert.assertEquals(-1, sumFirstAndLastDigit(-1));
        Assert.assertEquals(-1, sumFirstAndLastDigit(-123));
    }

    @Test
    public void sumFirstAndLastDigitPositiveTest() {
        Assert.assertEquals(4, sumFirstAndLastDigit(1000000003));
        Assert.assertEquals(2, sumFirstAndLastDigit(1));
        Assert.assertEquals(4, sumFirstAndLastDigit(252));
        Assert.assertEquals(9, sumFirstAndLastDigit(257));
        Assert.assertEquals(0, sumFirstAndLastDigit(0));
        Assert.assertEquals(10, sumFirstAndLastDigit(5));
    }


}
