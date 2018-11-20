package section_04.exercises;

import org.junit.Assert;
import org.junit.Test;

public class DecimalComparatorTest {
    @Test
    public void areEqualByThreeDecimalPlacesTest() {
        Assert.assertTrue(DecimalComparator.areEqualByThreeDecimalPlaces(-3.1756, -3.175));
        Assert.assertTrue(DecimalComparator.areEqualByThreeDecimalPlaces(-3.1756, -3.175123123));
        Assert.assertTrue(DecimalComparator.areEqualByThreeDecimalPlaces(3.0, 3.0));
        Assert.assertFalse(DecimalComparator.areEqualByThreeDecimalPlaces(-3.1756, 3.1757));
        Assert.assertFalse(DecimalComparator.areEqualByThreeDecimalPlaces(3.174, 3.175));

    }
}
