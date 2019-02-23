package section_05.exercises;

import org.junit.Assert;
import org.junit.Test;

public class DiagonalStarTest {
    @Test
    public void InvalidValueTest() {
        Assert.assertEquals("Invalid Value", DiagonalStart.printSquareStar(-1));
        Assert.assertEquals("Invalid Value", DiagonalStart.printSquareStar(0));
        Assert.assertEquals("Invalid Value", DiagonalStart.printSquareStar(4));
    }
    
}
