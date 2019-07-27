package section_05.challenges;

import org.junit.Test;

import java.util.Arrays;

import static org.junit.Assert.*;
import static section_05.challenges.PrimeFinder.find;
import static section_05.challenges.PrimeFinder.isPrime;

public class PrimeFinderTest {
    @Test
    public void isPrimeTest() {
        assertTrue(isPrime(2));
        assertTrue(isPrime(3));
        assertTrue(isPrime(5));
        assertTrue(isPrime(29));
        assertTrue(isPrime(7919));

        assertFalse(isPrime(-1));
        assertFalse(isPrime(4));
        assertFalse(isPrime(8));
        assertFalse(isPrime(15828));
    }

    @Test
    public void findTest() {
        assertEquals(Arrays.asList(2, 3, 5), find(0, 5));
        assertEquals(Arrays.asList(2, 3, 5), find(0, 100));
        assertEquals(Arrays.asList(6551, 6553, 6563), find(6551, 6563));
    }
}
