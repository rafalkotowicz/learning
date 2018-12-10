package section_05.exercises;

import org.junit.Assert;
import org.junit.Test;

public class FlourPackerTest {
    @Test
    public void canPackInvalidParametersTest() {
        Assert.assertFalse(FlourPacker.canPack(-1, 0, 0));
        Assert.assertFalse(FlourPacker.canPack(0, -1, 0));
        Assert.assertFalse(FlourPacker.canPack(0, 0, -1));
        Assert.assertFalse(FlourPacker.canPack(-1, -1, -1));
    }

    @Test
    public void canPackPositiveTest() {
        Assert.assertTrue(FlourPacker.canPack(2,0,10));
        Assert.assertTrue(FlourPacker.canPack(3,0,10));
        Assert.assertTrue(FlourPacker.canPack(25,0,75));
        Assert.assertTrue(FlourPacker.canPack(26,0,75));

        Assert.assertTrue(FlourPacker.canPack(2,4,13));
        Assert.assertTrue(FlourPacker.canPack(2,1,10));
        Assert.assertTrue(FlourPacker.canPack(2,6,16));
    }

    @Test
    public void canPackNegativeTest() {
        Assert.assertFalse(FlourPacker.canPack(2,0,11));
        Assert.assertFalse(FlourPacker.canPack(2,4,20));

        Assert.assertFalse(FlourPacker.canPack(2,1,7));
        Assert.assertFalse(FlourPacker.canPack(1,0,2));
    }
}
