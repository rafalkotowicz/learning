package section_06.exercises;

import org.junit.Assert;
import org.junit.Test;
import section_06.exercises.cylinder.Circle;
import section_06.exercises.cylinder.Cylinder;

import static utils.Constants.TOLERANCE;

public class CylinderTest {
    @Test
    public void negativeRadiusIsInitializedToZeroTest() {
        Circle circle = new Circle(-10.123);
        Assert.assertEquals(0, circle.getRadius(), TOLERANCE);
    }

    @Test
    public void getAreaTest() {
        Circle circle = new Circle(2.0);
        Assert.assertEquals(12.566370614359172, circle.getArea(), TOLERANCE);
    }

    @Test
    public void negativeHeightInitializedToZeroTest() {
        Cylinder cylinder = new Cylinder(2, -3);
        Assert.assertEquals(0.0, cylinder.getHeight(), TOLERANCE);
    }

    @Test
    public void getVolumeTest() {
        Cylinder cylinder = new Cylinder(2, 3);
        Assert.assertEquals(37.69911184307752, cylinder.getVolume(), TOLERANCE);
    }
}
