package section_03;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static section_03.challenges.ByteShortInLong.doMath;

public class ByteShortInLongTest {

    @Test
    public void doMathTest() {
        byte myByte = 100;
        short myShort = 10_000;
        int myInt = 1_000_000_000;

        long expectedValue = 10_000_151_000L;

        assertEquals(expectedValue, doMath(myByte, myShort, myInt));
    }
}
