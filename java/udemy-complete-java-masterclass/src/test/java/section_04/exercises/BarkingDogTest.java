package section_04.exercises;

import org.junit.Test;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import static section_04.exercises.BarkingDog.bark;

public class BarkingDogTest {

    @Test
    public void barkTest() {
        assertTrue(bark(true, 1));
        assertFalse(bark(false, 2));
        assertFalse(bark(true, 8));
        assertFalse(bark(true, -1));
    }
}
