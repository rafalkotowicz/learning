package section_05.challenges;

import org.junit.Assert;
import org.junit.Test;

public class FindNumbersTest {
    @Test
    public void sumOfNumbersDivisileBy3And5Test() {
        Assert.assertEquals(0, FindNumbers.sumOfNumbersDivisibleBy3And5(0,1,0));
        Assert.assertEquals(15, FindNumbers.sumOfNumbersDivisibleBy3And5(0,15,1000));
        Assert.assertEquals(90, FindNumbers.sumOfNumbersDivisibleBy3And5(1,1000,3));
    }
}
