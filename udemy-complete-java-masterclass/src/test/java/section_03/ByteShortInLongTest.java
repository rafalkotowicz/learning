package section_03;

import org.junit.Assert;
import org.junit.Test;

public class ByteShortInLongTest {

    @Test
    public void doMathTest() {
        byte myByte = 100;
        short myShort = 10_000;
        int myInt = 1_000_000_000;

        long expectedValue = 10_000_151_000L;

        Assert.assertEquals(expectedValue, ByteShortInLong.doMath(myByte, myShort, myInt));
    }
}
