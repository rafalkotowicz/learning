package section_05.exercises;

import org.junit.Assert;
import org.junit.Test;

import static section_05.exercises.SharedDigit.hasSharedDigit;

public class SharedDigitTest {
    @Test
    public void hasShareDigitTest() {
//        Assert.assertFalse(hasSharedDigit(9, 99));
//        Assert.assertFalse(hasSharedDigit(11, 100));
//        Assert.assertFalse(hasSharedDigit(1, 1));
//        Assert.assertFalse(hasSharedDigit(1, 100));
//        Assert.assertTrue(hasSharedDigit(12, 23));
//        Assert.assertTrue(hasSharedDigit(15, 55));
        Assert.assertTrue(hasSharedDigit(12, 13));
    }
}
