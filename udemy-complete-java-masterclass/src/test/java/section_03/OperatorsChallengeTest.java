package section_03;

import org.junit.Test;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import static section_03.challenges.OperatorsChallenge.isLowerOrEqualToLimit;

public class OperatorsChallengeTest {

    @Test
    public void isLowerOrEqualToLimitTest() {
        assertTrue(isLowerOrEqualToLimit(20, 80, 25, 40, 20));
        assertFalse(isLowerOrEqualToLimit(1, 2, 3, 5, 2));
    }
}
