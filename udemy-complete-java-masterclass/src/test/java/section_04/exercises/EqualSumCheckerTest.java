package section_04.exercises;

import org.junit.Assert;
import org.junit.Test;

import static section_04.exercises.EqualSumChecker.*;

public class EqualSumCheckerTest {
    @Test
    public void hasEqualSumTest() {
        Assert.assertFalse(hasEqualSum(1,1,1));
        Assert.assertTrue(hasEqualSum(1,1,2));
        Assert.assertTrue(hasEqualSum(1,-1,0));
    }
}
