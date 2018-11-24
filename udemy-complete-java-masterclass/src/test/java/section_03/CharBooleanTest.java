package section_03;

import org.junit.Assert;
import org.junit.Test;
import section_03.challenges.CharBoolean;

public class CharBooleanTest {

    @Test
    public void findUnicodePositionTest() {
        Assert.assertEquals("Invalid Unicode position", 97, CharBoolean.findUnicodePosition('a'));
        Assert.assertEquals("Invalid Unicode position", 66, CharBoolean.findUnicodePosition('B'));
        Assert.assertEquals("Invalid Unicode position", 49, CharBoolean.findUnicodePosition('1'));
    }
}

