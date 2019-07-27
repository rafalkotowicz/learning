package section_07.challenges;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static java.lang.System.setOut;
import static org.junit.Assert.assertEquals;
import static utils.Constants.TOLERANCE;

public class PrinterTest {
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
    public void refilTonerTest() {
        Printer printer = new Printer(75);
        assertEquals(75, printer.getTonerLevel(), TOLERANCE);
        printer.refilToner();
        assertEquals(100, printer.getTonerLevel(), TOLERANCE);
    }

    @Test
    public void pagesAreCountedDuringPrintingTest() {
        Printer printer = new Printer();
        assertEquals(0, printer.getPrintedPagesCount());
        printer.printPages(10);
        assertEquals(10, printer.getPrintedPagesCount());
    }

    @Test
    public void tonerLevelIsDecreasingDuringPrintoutTest() {
        Printer printer = new Printer(75);
        assertEquals(75, printer.getTonerLevel(), TOLERANCE);
        printer.printPages(200);
        assertEquals(55, printer.getTonerLevel(), TOLERANCE);
    }

    @Test
    public void sheetsAreCounterDuringPrintingTest() {
        Printer printer = new Printer();
        assertEquals(0, printer.usedSheetsOfPaper());
        printer.printPages(10);
        assertEquals(10, printer.usedSheetsOfPaper());
    }

    @Test
    public void duplexPrintingUsesHalfOfSheetsOfPaperTest() {
        Printer printer = new Printer();
        assertEquals(0, printer.usedSheetsOfPaper());
        printer.printPages(50, false);
        assertEquals(50, printer.usedSheetsOfPaper());
        printer.printPages(50, true);
        assertEquals(75, printer.usedSheetsOfPaper());
        printer.printPages(3, true);
        assertEquals(77, printer.usedSheetsOfPaper());
    }

    @Test
    public void printingOverTonerCapacityTest() {
        Printer printer = new Printer(10);
        printer.printPages(120, true);
        assertEquals(50, printer.usedSheetsOfPaper());
        assertEquals(100, printer.getPrintedPagesCount());
        assertEquals(0, printer.getTonerLevel(), TOLERANCE);
        assertEquals("Toner empty! Printed only 100 out of 120 requested pages", caughtOutput.toString());
    }
}
