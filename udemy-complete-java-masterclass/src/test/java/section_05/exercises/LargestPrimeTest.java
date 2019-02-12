package section_05.exercises;

import org.junit.Assert;
import org.junit.Test;

public class LargestPrimeTest {

    @Test
    public void numberBelowTwoShouldReturnNegativeOneTest() {
        Assert.assertEquals(-1, LargestPrime.getLargestPrime(-10));
        Assert.assertEquals(-1, LargestPrime.getLargestPrime(-1));
        Assert.assertEquals(-1, LargestPrime.getLargestPrime(0));
        Assert.assertEquals(-1, LargestPrime.getLargestPrime(1));
    }

    @Test
    public void largestPrimeFactorTest() {
        Assert.assertEquals(7, LargestPrime.getLargestPrime(21));
        Assert.assertEquals(31, LargestPrime.getLargestPrime(217));
        Assert.assertEquals(5, LargestPrime.getLargestPrime(45));
        Assert.assertEquals(31, LargestPrime.getLargestPrime(31));
    }
}
