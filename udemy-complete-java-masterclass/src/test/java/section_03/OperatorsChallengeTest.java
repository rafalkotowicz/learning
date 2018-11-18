package section_03;

import org.junit.Assert;
import org.junit.Test;

public class OperatorsChallengeTest {

    @Test
    public void isLowerOrEqualToLimitTest() {
        Assert.assertTrue(OperatorsChallenge.isLowerOrEqualToLimit(20, 80, 25, 40, 20));
        Assert.assertFalse(OperatorsChallenge.isLowerOrEqualToLimit(1, 2, 3, 5, 2));
    }
}
