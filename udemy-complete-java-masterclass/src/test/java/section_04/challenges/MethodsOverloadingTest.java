package section_04.challenges;

import org.junit.Assert;
import org.junit.Test;

import static section_04.challenges.MethodsOverloading.calcImperialToMetric;
import static section_04.challenges.MethodsOverloading.toHourMinutesSeconds;

public class MethodsOverloadingTest {
    private double MAX_DELTA = 0.001;

    @Test
    public void calcImperialToMetric2ParamsTest() {
        Assert.assertEquals(342.90, calcImperialToMetric(11, 3), MAX_DELTA);
        Assert.assertEquals(2.54, calcImperialToMetric(0, 1), MAX_DELTA);
        Assert.assertEquals(365.76, calcImperialToMetric(12, 0), MAX_DELTA);
        Assert.assertEquals(0, calcImperialToMetric(0, 0), MAX_DELTA);
        Assert.assertEquals(-1, calcImperialToMetric(1, 13), MAX_DELTA);
        Assert.assertEquals(-1, calcImperialToMetric(-1, 0), MAX_DELTA);
        Assert.assertEquals(-1, calcImperialToMetric(0, -1), MAX_DELTA);
        Assert.assertEquals(-1, calcImperialToMetric(-1, -1), MAX_DELTA);
    }

    @Test
    public void calcImperialToMetric1ParamTest() {
        Assert.assertEquals(27.94, calcImperialToMetric(11), MAX_DELTA);
        Assert.assertEquals(2.54, calcImperialToMetric(1), MAX_DELTA);
        Assert.assertEquals(2540.00, calcImperialToMetric(1000), MAX_DELTA);
        Assert.assertEquals(0, calcImperialToMetric(0, 0), MAX_DELTA);
        Assert.assertEquals(-1, calcImperialToMetric(-1, 0), MAX_DELTA);
    }

    @Test
    public void toHourMinutesSeconds1ParamTest() {
        Assert.assertEquals("01h 00m 00s", toHourMinutesSeconds(3600));
        Assert.assertEquals("01h 10m 01s", toHourMinutesSeconds(4201));
        Assert.assertEquals("00h 00m 00s", toHourMinutesSeconds(0));
        Assert.assertEquals("Invalid Parameter", toHourMinutesSeconds(-1));
    }

    @Test
    public void toHourMinutesSeconds2ParamsTest() {
        Assert.assertEquals("01h 00m 00s", toHourMinutesSeconds(60, 0));
        Assert.assertEquals("01h 12m 01s", toHourMinutesSeconds(72, 1));
        Assert.assertEquals("Invalid Parameter - seconds", toHourMinutesSeconds(72, -1));
        Assert.assertEquals("Invalid Parameter - seconds", toHourMinutesSeconds(72, 60));
        Assert.assertEquals("Invalid Parameter - seconds", toHourMinutesSeconds(72, 61));
        Assert.assertEquals("Invalid Parameter - minutes", toHourMinutesSeconds(-1, 1));
    }
}
