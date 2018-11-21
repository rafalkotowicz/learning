package section_04.exercises;

import org.junit.Assert;
import org.junit.Test;

import static section_04.exercises.DecimalComparator.*;

public class DecimalComparatorTest {
    @Test
    public void areEqualByThreeDecimalPlacesTest() {
        Assert.assertTrue(areEqualByThreeDecimalPlaces(-3.1756, -3.175));
        Assert.assertTrue(areEqualByThreeDecimalPlaces(-3.1756, -3.175123123));
        Assert.assertTrue(areEqualByThreeDecimalPlaces(3.0, 3.0));
        Assert.assertFalse(areEqualByThreeDecimalPlaces(-3.1756, 3.1757));
        Assert.assertFalse(areEqualByThreeDecimalPlaces(3.174, 3.175));

    }
}
