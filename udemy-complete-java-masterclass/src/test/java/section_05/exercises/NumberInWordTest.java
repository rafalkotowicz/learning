package section_05.exercises;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.Assert.assertEquals;
import static section_05.exercises.NumberInWord.printNumberInWord;

public class NumberInWordTest {
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
    public void printNumberInWordTest() {
        printNumberInWord(1);
        assertEquals("ONE", caughtOutput.toString());
        caughtOutput.reset();
        printNumberInWord(5);
        assertEquals("FIVE", caughtOutput.toString());
        caughtOutput.reset();
    }
}

