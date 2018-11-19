package section_04.exercises;

import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

public class MegaBytesConverterTest {
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();
    private final PrintStream originalOut = System.out;

    @Before
    public void setUpStreams() {
        System.setOut(new PrintStream(outContent));
    }

    @After
    public void restoreStreams() {
        System.setOut(originalOut);
    }

    @Test
    public void printMegaBytesAndKiloBytesPositiveInputTest() {
        MegaBytesConverter.printMegaBytesAndKiloBytes(100);
        Assert.assertEquals("100 KB = 0 MB and 100 KB", outContent.toString());
        outContent.reset();
        MegaBytesConverter.printMegaBytesAndKiloBytes(1024);
        Assert.assertEquals("1024 KB = 1 MB and 0 KB", outContent.toString());
        outContent.reset();
        MegaBytesConverter.printMegaBytesAndKiloBytes(4097);
        Assert.assertEquals("4097 KB = 4 MB and 1 KB", outContent.toString());
        outContent.reset();
        MegaBytesConverter.printMegaBytesAndKiloBytes(8191);
        Assert.assertEquals("8191 KB = 7 MB and 1023 KB", outContent.toString());
    }

    @Test
    public void printMegaBytesAndKiloBytesNegativeInputTest() {
        MegaBytesConverter.printMegaBytesAndKiloBytes(-100);
        Assert.assertEquals("Invalid Value", outContent.toString());
    }
}
