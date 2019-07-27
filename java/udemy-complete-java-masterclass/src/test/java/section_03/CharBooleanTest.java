package section_03;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static section_03.challenges.CharBoolean.findUnicodePosition;

public class CharBooleanTest {

    @Test
    public void findUnicodePositionTest() {
        assertEquals("Invalid Unicode position", 97, findUnicodePosition('a'));
        assertEquals("Invalid Unicode position", 66, findUnicodePosition('B'));
        assertEquals("Invalid Unicode position", 49, findUnicodePosition('1'));
    }
}

