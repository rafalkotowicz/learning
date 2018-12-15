package section_04.exercises;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static java.lang.System.setOut;
import static org.junit.Assert.assertEquals;
import static section_04.exercises.MegaBytesConverter.printMegaBytesAndKiloBytes;

public class MegaBytesConverterTest {
    private final ByteArrayOutputStream caughtOutput = new ByteArrayOutputStream();
    private final PrintStream originalOut = System.out;

    @Before
    public void setUpStreams() {
        setOut(new PrintStream(caughtOutput));
    }

    @After
    public void restoreStreams() {
        setOut(originalOut);
    }

    @Test
    public void printMegaBytesAndKiloBytesPositiveInputTest() {
        assertPrintout(100, "100 KB = 0 MB and 100 KB");
        assertPrintout(1024, "1024 KB = 1 MB and 0 KB");
        assertPrintout(4097, "4097 KB = 4 MB and 1 KB");
        assertPrintout(8191, "8191 KB = 7 MB and 1023 KB");
    }

    @Test
    public void printMegaBytesAndKiloBytesNegativeInputTest() {
        assertPrintout(-1, "Invalid Value");
        assertPrintout(-10, "Invalid Value");
        assertPrintout(-100, "Invalid Value");
    }

    private void assertPrintout(int i, String s) {
        printMegaBytesAndKiloBytes(i);
        assertEquals(s, caughtOutput.toString());
        caughtOutput.reset();
    }
}
