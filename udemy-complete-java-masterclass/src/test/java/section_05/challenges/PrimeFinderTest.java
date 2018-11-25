package section_05.challenges;

import org.junit.Assert;
import org.junit.Test;

import java.util.Arrays;

public class PrimeFinderTest {
    @Test
    public void isPrimeTest() {
        Assert.assertTrue(PrimeFinder.isPrime(2));
        Assert.assertTrue(PrimeFinder.isPrime(3));
        Assert.assertTrue(PrimeFinder.isPrime(5));
        Assert.assertTrue(PrimeFinder.isPrime(29));
        Assert.assertTrue(PrimeFinder.isPrime(7919));

        Assert.assertFalse(PrimeFinder.isPrime(-1));
        Assert.assertFalse(PrimeFinder.isPrime(4));
        Assert.assertFalse(PrimeFinder.isPrime(8));
        Assert.assertFalse(PrimeFinder.isPrime(15828));
    }

    @Test
    public void findTest() {
        Assert.assertEquals(Arrays.asList(2, 3, 5), PrimeFinder.find(0, 5));
        Assert.assertEquals(Arrays.asList(2, 3, 5), PrimeFinder.find(0, 100));
        Assert.assertEquals(Arrays.asList(6551, 6553, 6563), PrimeFinder.find(6551, 6563));
    }
}
