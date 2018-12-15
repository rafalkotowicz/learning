package section_05.exercises;

import org.junit.Test;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import static section_05.exercises.NumberPalindrome.isPalindrome;

public class NumberPalindromeTest {
    @Test
    public void isPalindromeTest() {
        assertTrue(isPalindrome(1001));
        assertTrue(isPalindrome(10001));
        assertTrue(isPalindrome(-10001));

        assertFalse(isPalindrome(102));
        assertFalse(isPalindrome(-102));
    }
}
