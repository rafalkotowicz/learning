package section_04.challenges;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static section_04.challenges.MethodsOverloading.calcImperialToMetric;
import static section_04.challenges.MethodsOverloading.toHourMinutesSeconds;

public class MethodsOverloadingTest {
    private double MAX_DELTA = 0.001;

    @Test
    public void calcImperialToMetric2ParamsTest() {
        assertEquals(342.90, calcImperialToMetric(11, 3), MAX_DELTA);
        assertEquals(2.54, calcImperialToMetric(0, 1), MAX_DELTA);
        assertEquals(365.76, calcImperialToMetric(12, 0), MAX_DELTA);
        assertEquals(0, calcImperialToMetric(0, 0), MAX_DELTA);
        assertEquals(-1, calcImperialToMetric(1, 13), MAX_DELTA);
        assertEquals(-1, calcImperialToMetric(-1, 0), MAX_DELTA);
        assertEquals(-1, calcImperialToMetric(0, -1), MAX_DELTA);
        assertEquals(-1, calcImperialToMetric(-1, -1), MAX_DELTA);
    }

    @Test
    public void calcImperialToMetric1ParamTest() {
        assertEquals(27.94, calcImperialToMetric(11), MAX_DELTA);
        assertEquals(2.54, calcImperialToMetric(1), MAX_DELTA);
        assertEquals(2540.00, calcImperialToMetric(1000), MAX_DELTA);
        assertEquals(0, calcImperialToMetric(0, 0), MAX_DELTA);
        assertEquals(-1, calcImperialToMetric(-1, 0), MAX_DELTA);
    }

    @Test
    public void toHourMinutesSeconds1ParamTest() {
        assertEquals("01h 00m 00s", toHourMinutesSeconds(3600));
        assertEquals("01h 10m 01s", toHourMinutesSeconds(4201));
        assertEquals("00h 00m 00s", toHourMinutesSeconds(0));
        assertEquals("Invalid Parameter", toHourMinutesSeconds(-1));
    }

    @Test
    public void toHourMinutesSeconds2ParamsTest() {
        assertEquals("01h 00m 00s", toHourMinutesSeconds(60, 0));
        assertEquals("01h 12m 01s", toHourMinutesSeconds(72, 1));
        assertEquals("Invalid Parameter - seconds", toHourMinutesSeconds(72, -1));
        assertEquals("Invalid Parameter - seconds", toHourMinutesSeconds(72, 60));
        assertEquals("Invalid Parameter - seconds", toHourMinutesSeconds(72, 61));
        assertEquals("Invalid Parameter - minutes", toHourMinutesSeconds(-1, 1));
    }
}
