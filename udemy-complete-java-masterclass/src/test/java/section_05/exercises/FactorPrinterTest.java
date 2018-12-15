package section_05.exercises;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static section_05.exercises.FactorPrinter.findFactors;

public class FactorPrinterTest {
    @Test
    public void findFactorsInvalidInputTest() {
        assertEquals("Invalid Value", findFactors(0));
        assertEquals("Invalid Value", findFactors(-11111));
    }

    @Test
    public void findFactorsTest() {
        assertEquals("1 2 3 6", findFactors(6));
        assertEquals("1 2 4 8 16 32", findFactors(32));
        assertEquals("1 2 4 8 16 32 64", findFactors(64));
        assertEquals("1 2 4 8 16 32 64 128", findFactors(128));
    }
}
