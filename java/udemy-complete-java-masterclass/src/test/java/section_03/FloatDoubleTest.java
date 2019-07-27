package section_03;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static section_03.challenges.FloatDouble.poundToKiloConverter;

public class FloatDoubleTest {
    @Test
    public void poundToKiloConverterTest() {
        double expectedValue = 4.5359237D;
        double delta = 0.001D;
        assertEquals(expectedValue, poundToKiloConverter(10D), delta);
    }
}
