package section_03;

import org.junit.Assert;
import org.junit.Test;
import section_03.challenges.FloatDouble;

public class FloatDoubleTest {
    @Test
    public void poundToKiloConverterTest() {
        double expectedValue = 4.5359237D;
        double delta = 0.001D;
        Assert.assertEquals(expectedValue, FloatDouble.poundToKiloConverter(10D), delta);
    }
}
