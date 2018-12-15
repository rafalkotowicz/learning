package section_05.challenges;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static section_05.challenges.FindNumbers.sumOfNumbersDivisibleBy3And5;

public class FindNumbersTest {
    @Test
    public void sumOfNumbersDivisibleBy3And5Test() {
        assertEquals(0, sumOfNumbersDivisibleBy3And5(0,1,0));
        assertEquals(15, sumOfNumbersDivisibleBy3And5(0,15,1000));
        assertEquals(90, sumOfNumbersDivisibleBy3And5(1,1000,3));
    }
}
