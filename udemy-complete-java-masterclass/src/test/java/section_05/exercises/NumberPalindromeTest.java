package section_05.exercises;

import org.junit.Assert;
import org.junit.Test;

public class NumberPalindromeTest {
    @Test
    public void isPalindromeTest() {
        Assert.assertTrue(NumberPalindrome.isPalindrome(1001));
        Assert.assertTrue(NumberPalindrome.isPalindrome(10001));
        Assert.assertTrue(NumberPalindrome.isPalindrome(-10001));

        Assert.assertFalse(NumberPalindrome.isPalindrome(102));
        Assert.assertFalse(NumberPalindrome.isPalindrome(-102));
    }
}
