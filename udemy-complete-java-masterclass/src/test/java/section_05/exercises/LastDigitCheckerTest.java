package section_05.exercises;

import org.junit.Assert;
import org.junit.Test;

import static section_05.exercises.LastDigitChecker.*;

public class LastDigitCheckerTest {
    @Test
    public void hasSameLastDigitInputValidityTest() {
        Assert.assertFalse(hasSameLastDigit(123,124,-1));
        Assert.assertFalse(hasSameLastDigit(123,-1,1));
        Assert.assertFalse(hasSameLastDigit(-1,1,1));
    }
    @Test
    public void hasSameLastDigitTest() {
        Assert.assertFalse(hasSameLastDigit(23,24,25));
        Assert.assertFalse(hasSameLastDigit(23,32,41));

        Assert.assertTrue(hasSameLastDigit(41,22,71));
        Assert.assertTrue(hasSameLastDigit(23,31,41));
        Assert.assertTrue(hasSameLastDigit(23,33,41));
    }
}
