package section_03;

import org.junit.Assert;
import org.junit.Test;
import section_03.challenges.CharBoolean;

public class CharBooleanTest {

    @Test
    public void findUnicodePositionTest() {
        Assert.assertEquals("Invalid Unicode position", 174, CharBoolean.findUnicodePosition('®'));
        Assert.assertEquals("Invalid Unicode position", 321, CharBoolean.findUnicodePosition('Ł'));
        Assert.assertEquals("Invalid Unicode position", 243, CharBoolean.findUnicodePosition('ó'));
    }
}

