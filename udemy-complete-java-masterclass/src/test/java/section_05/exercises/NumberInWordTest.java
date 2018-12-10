package section_05.exercises;

import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

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
        NumberInWord.printNumberInWord(1);
        Assert.assertEquals("ONE", caughtOutput.toString());
        caughtOutput.reset();
        NumberInWord.printNumberInWord(5);
        Assert.assertEquals("FIVE", caughtOutput.toString());
        caughtOutput.reset();
    }
}

