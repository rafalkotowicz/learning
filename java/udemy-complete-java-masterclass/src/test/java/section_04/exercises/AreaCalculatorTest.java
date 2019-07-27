package section_04.exercises;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static section_04.exercises.AreaCalculator.area;

public class AreaCalculatorTest {

    public static final double ACCEPTABLE_ERROR = 0.001;

    @Test
    public void area1ParamTest() {
        assertEquals(3.141592d, area(1.0), ACCEPTABLE_ERROR);
        assertEquals(12.566368d, area(2.0), ACCEPTABLE_ERROR);
        assertEquals(0.0d, area(0.0), ACCEPTABLE_ERROR);
        assertEquals(-1.0d, area(-0.00001d), ACCEPTABLE_ERROR);
    }

    @Test
    public void area2ParamsTest() {
        assertEquals(36.0d, area(4.0, 9.0), ACCEPTABLE_ERROR);
        assertEquals(300.1152d, area(13.44, 22.33), ACCEPTABLE_ERROR);
        assertEquals(-1.0, area(-1.0, -1.0), ACCEPTABLE_ERROR);
        assertEquals(-1.0, area(13.44, -1.0), ACCEPTABLE_ERROR);
        assertEquals(-1.0, area(-1.0, 22.33), ACCEPTABLE_ERROR);
        assertEquals(0, area(0, 0), ACCEPTABLE_ERROR);
    }
}
