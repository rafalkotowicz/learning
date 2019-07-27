package section_04.exercises;

import org.junit.Test;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import static section_04.exercises.TeenNumberChecker.hasTeen;

public class TeenNumberCheckerTest {
    @Test
    public void hasTeenTest() {
        assertTrue(hasTeen(9, 99, 19));
        assertTrue(hasTeen(23, 15, 42));
        assertFalse(hasTeen(23, 24, 25));
    }
}
