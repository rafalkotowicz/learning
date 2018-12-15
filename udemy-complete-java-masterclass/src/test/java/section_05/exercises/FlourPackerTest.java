package section_05.exercises;

import org.junit.Test;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import static section_05.exercises.FlourPacker.canPack;

public class FlourPackerTest {
    @Test
    public void canPackInvalidParametersTest() {
        assertFalse(canPack(-1, 0, 0));
        assertFalse(canPack(0, -1, 0));
        assertFalse(canPack(0, 0, -1));
        assertFalse(canPack(-1, -1, -1));
    }

    @Test
    public void canPackPositiveTest() {
        assertTrue(canPack(2,0,10));
        assertTrue(canPack(3,0,10));
        assertTrue(canPack(25,0,75));
        assertTrue(canPack(26,0,75));

        assertTrue(canPack(2,4,13));
        assertTrue(canPack(2,1,10));
        assertTrue(canPack(2,6,16));
    }

    @Test
    public void canPackNegativeTest() {
        assertFalse(canPack(2,0,11));
        assertFalse(canPack(2,4,20));

        assertFalse(canPack(2,1,7));
        assertFalse(canPack(1,0,2));
    }
}
