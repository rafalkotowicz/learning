package section_04.exercises;

import org.junit.Assert;
import org.junit.Test;

import static section_04.exercises.TeenNumberChecker.*;

public class TeenNumberCheckerTest {
    @Test
    public void hasTeenTest() {
        Assert.assertTrue(hasTeen(9, 99, 19));
        Assert.assertTrue(hasTeen(23, 15, 42));
        Assert.assertFalse(hasTeen(23, 24, 25));
    }
}
