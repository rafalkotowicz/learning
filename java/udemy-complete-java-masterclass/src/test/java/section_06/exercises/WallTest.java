package section_06.exercises;

import org.junit.Assert;
import org.junit.Test;

import static utils.Constants.TOLERANCE;

public class WallTest {
    @Test
    public void contructorShouldSetZeroIfNegativeValueGivenTest() {
        Wall wall = new Wall(-1, -1);
        Assert.assertEquals(0, wall.getHeight(), TOLERANCE);
        Assert.assertEquals(0, wall.getWidth(), TOLERANCE);
    }

    @Test
    public void contructorStoresValidWallDimensionTest() {
        Wall wall = new Wall(3, 5);
        Assert.assertEquals(3, wall.getWidth(), TOLERANCE);
        Assert.assertEquals(5, wall.getHeight(), TOLERANCE);
    }

    @Test
    public void settingNegativeWallDimensionsIsImpossibleTest() {
        Wall wall = new Wall();
        wall.setWidth(-1.2);
        Assert.assertEquals(0, wall.getWidth(), TOLERANCE);
        wall.setHeight(-1.3);
        Assert.assertEquals(0, wall.getHeight(), TOLERANCE);
    }

    @Test
    public void getAreaReturnsWallAreaTest() {
        Wall wall = new Wall(3, 3.5);
        Assert.assertEquals(10.5, wall.getArea(), TOLERANCE);
    }
}
