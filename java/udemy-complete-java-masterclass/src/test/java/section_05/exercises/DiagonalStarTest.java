package section_05.exercises;

import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static section_05.exercises.DiagonalStar.printSquareStar;

public class DiagonalStarTest {
    private ByteArrayOutputStream caughtOutput = new ByteArrayOutputStream();
    private PrintStream originaOutputStream = System.out;

    @Before
    public void catchOutput() {
        System.setOut(new PrintStream(caughtOutput));
    }

    @After
    public void restoreOutputStream() {
        System.setOut(originaOutputStream);
    }

    @Test
    public void InvalidValueTest() {
        printSquareStar(-1);
        Assert.assertEquals("Invalid Value", caughtOutput.toString());
        caughtOutput.reset();
        printSquareStar(0);
        Assert.assertEquals("Invalid Value", caughtOutput.toString());
        caughtOutput.reset();
        printSquareStar(4);
        Assert.assertEquals("Invalid Value", caughtOutput.toString());
    }

    //* In the first or last row
    //* In the first or last column
    //* When the row number equals the column number
    //* When the column number equals rowCount - currentRow + 1 (where currentRow is current row number)
    @Test
    public void printDiagonalStartTest() {
        String expectedOutput = "*****"+System.lineSeparator()+
                                "** **"+System.lineSeparator()+
                                "* * *"+System.lineSeparator()+
                                "** **"+System.lineSeparator()+
                                "*****"+System.lineSeparator();
        printSquareStar(5);
        Assert.assertEquals(expectedOutput, caughtOutput.toString());
    }
}
