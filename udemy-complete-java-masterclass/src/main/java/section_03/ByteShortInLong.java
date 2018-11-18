package section_03;

public class ByteShortInLong {

    public static long doMath(byte myByte, short myShort, int myInt) {
        return (myByte + myShort + myInt) * 10L + 50_000L;
    }
}
