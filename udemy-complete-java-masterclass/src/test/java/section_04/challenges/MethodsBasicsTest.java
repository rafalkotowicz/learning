package section_04.challenges;

import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static section_04.challenges.MethodsBasics.calculateHighScorePosition;

public class MethodsBasicsTest {
    private final ByteArrayOutputStream caughtOutput = new ByteArrayOutputStream();
    private final PrintStream originalOut = System.out;

    @Before
    public void setUpStreams() {
        System.setOut(new PrintStream(caughtOutput));
    }

    @After
    public void restoreStreams() {
        System.setOut(originalOut);
    }


    @Test
    public void displayHighScorePositionTest() {
        MethodsBasics.displayHighScorePosition("Tim", 2);
        Assert.assertEquals("Tim managed to get into position 2 on the high score table", caughtOutput.toString());
        caughtOutput.reset();
    }

    @Test
    public void calculateHighScorePositionTest() {
        Assert.assertEquals(1, calculateHighScorePosition(1500));
        Assert.assertEquals(1, calculateHighScorePosition(1000));
        Assert.assertEquals(2, calculateHighScorePosition(900));
        Assert.assertEquals(2, calculateHighScorePosition(500));
        Assert.assertEquals(3, calculateHighScorePosition(499));
        Assert.assertEquals(3, calculateHighScorePosition(100));
        Assert.assertEquals(4, calculateHighScorePosition(99));
        Assert.assertEquals(4, calculateHighScorePosition(-1));
    }
}
