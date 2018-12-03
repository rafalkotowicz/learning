package section_05.exercises;

import org.junit.Assert;
import org.junit.Test;

import static section_05.exercises.GreatestCommonDivisor.getGreatestCommonDivisor;

public class GreatestCommonDivisorTest {
    @Test
    public void getGreatestCommonDivisorInvalidInputTest() {
        Assert.assertEquals(-1, getGreatestCommonDivisor(1, 1));
        Assert.assertEquals(-1, getGreatestCommonDivisor(1, 10));
        Assert.assertEquals(-1, getGreatestCommonDivisor(10, 9));
    }

    @Test
    public void getGreatestCommonDivisorTest() {
        Assert.assertEquals(5, getGreatestCommonDivisor(25, 15));
        Assert.assertEquals(6, getGreatestCommonDivisor(12, 30));
        Assert.assertEquals(9, getGreatestCommonDivisor(81, 153));
    }

}
