package section_04.challenges;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static java.lang.System.setOut;
import static org.junit.Assert.assertEquals;
import static section_04.challenges.MethodsBasics.calculateHighScorePosition;

public class MethodsBasicsTest {
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
    public void displayHighScorePositionTest() {
        MethodsBasics.displayHighScorePosition("Tim", 2);
        assertEquals("Tim managed to get into position 2 on the high score table", caughtOutput.toString());
        caughtOutput.reset();
    }

    @Test
    public void calculateHighScorePositionTest() {
        assertEquals(1, calculateHighScorePosition(1500));
        assertEquals(1, calculateHighScorePosition(1000));
        assertEquals(2, calculateHighScorePosition(900));
        assertEquals(2, calculateHighScorePosition(500));
        assertEquals(3, calculateHighScorePosition(499));
        assertEquals(3, calculateHighScorePosition(100));
        assertEquals(4, calculateHighScorePosition(99));
        assertEquals(4, calculateHighScorePosition(-1));
    }
}
