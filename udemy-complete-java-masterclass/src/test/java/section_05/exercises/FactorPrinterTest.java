package section_05.exercises;

import org.junit.Assert;
import org.junit.Test;

import static section_05.exercises.FactorPrinter.*;

public class FactorPrinterTest {
    @Test
    public void findFactorsInvalidInputTest() {
        Assert.assertEquals("Invalid Value", findFactors(0));
        Assert.assertEquals("Invalid Value", findFactors(-11111));
    }

    @Test
    public void findFactorsTest() {
        Assert.assertEquals("1 2 3 6", findFactors(6));
        Assert.assertEquals("1 2 4 8 16 32", findFactors(32));
        Assert.assertEquals("1 2 4 8 16 32 64", findFactors(64));
        Assert.assertEquals("1 2 4 8 16 32 64 128", findFactors(128));
    }
}
