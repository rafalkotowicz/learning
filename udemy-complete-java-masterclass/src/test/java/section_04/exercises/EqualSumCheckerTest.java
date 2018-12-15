package section_04.exercises;

import org.junit.Test;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import static section_04.exercises.EqualSumChecker.hasEqualSum;

public class EqualSumCheckerTest {
    @Test
    public void hasEqualSumTest() {
        assertFalse(hasEqualSum(1,1,1));
        assertTrue(hasEqualSum(1,1,2));
        assertTrue(hasEqualSum(1,-1,0));
    }
}
