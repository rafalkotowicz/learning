package section_04.exercises;

import org.junit.Assert;
import org.junit.Test;

public class TeenNumberCheckerTest {
    @Test
    public void hasTeenTest() {
        Assert.assertTrue(TeenNumberChecker.hasTeen(9, 99, 19));
        Assert.assertTrue(TeenNumberChecker.hasTeen(23, 15, 42));
        Assert.assertFalse(TeenNumberChecker.hasTeen(23, 24, 25));
    }
}
