package section_04.exercises;

import org.junit.Test;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import static section_04.exercises.DecimalComparator.areEqualByThreeDecimalPlaces;

public class DecimalComparatorTest {
    @Test
    public void areEqualByThreeDecimalPlacesTest() {
        assertTrue(areEqualByThreeDecimalPlaces(-3.1756, -3.175));
        assertTrue(areEqualByThreeDecimalPlaces(-3.1756, -3.175123123));
        assertTrue(areEqualByThreeDecimalPlaces(3.0, 3.0));
        assertFalse(areEqualByThreeDecimalPlaces(-3.1756, 3.1757));
        assertFalse(areEqualByThreeDecimalPlaces(3.174, 3.175));

    }
}
