package section_06.exercises;

import org.junit.Test;
import section_06.exercises.poolarea.Cuboid;
import section_06.exercises.poolarea.Rectangle;

import static org.junit.Assert.assertEquals;
import static utils.Constants.TOLERANCE;

public class PoolAreaTest {
    @Test
    public void cannotSetNegativeValueForAnyDimensionOfThePoolTest() {
        Rectangle rectangle = new Rectangle(-3, -1);
        assertEquals(0, rectangle.getLength(), TOLERANCE);
        assertEquals(0, rectangle.getWidth(), TOLERANCE);

        Cuboid cuboid = new Cuboid(-3, -4, -5);
        assertEquals(0, cuboid.getLength(), TOLERANCE);
        assertEquals(0, cuboid.getWidth(), TOLERANCE);
        assertEquals(0, cuboid.getHeight(), TOLERANCE);
    }

    @Test
    public void getRectangleAreaTest() {
        Rectangle rectangle = new Rectangle(1, 3);
        assertEquals(3, rectangle.getArea(), TOLERANCE);
    }

    @Test
    public void getCuboidVolumeTest() {
        Cuboid cuboid = new Cuboid(1, 2, 3);
        assertEquals(6, cuboid.getVolume(), TOLERANCE);
    }
}
