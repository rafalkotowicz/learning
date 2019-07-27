package section_06.exercises;

import org.junit.Assert;
import org.junit.Test;

import static utils.Constants.TOLERANCE;

public class PointTest {
    @Test
    public void distanceXyGivenTest() {
        Point p1 = new Point(3, 4);
        Assert.assertEquals(5.0, p1.distance(0, 0), TOLERANCE);

        Point p2 = new Point(6, 5);
        Assert.assertEquals(7.810249675906654, p2.distance(0, 0), TOLERANCE);
    }

    @Test
    public void distanceToZeroZeroTest() {
        Point p2 = new Point(6, 5);
        Assert.assertEquals(7.810249675906654, p2.distance(), TOLERANCE);
    }

    @Test
    public void distanceBetweenTwoPointsTest() {
        Point first = new Point(6, 5);
        Point second = new Point(3, 1);
        Assert.assertEquals(5.0, first.distance(second), TOLERANCE);
    }
}
