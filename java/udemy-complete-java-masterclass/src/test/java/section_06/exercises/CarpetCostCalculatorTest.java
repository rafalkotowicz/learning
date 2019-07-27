package section_06.exercises;

import org.junit.Test;
import section_06.exercises.carpetCostCalculator.*;

import static org.junit.Assert.assertEquals;
import static utils.Constants.TOLERANCE;

public class CarpetCostCalculatorTest {

    @Test
    public void getFloorAreaTest() {
        Floor floor = new Floor(1.1,3);
        assertEquals(3.3, floor.getArea(), TOLERANCE);
    }

    @Test
    public void settingNegativeFloorDimensionsShouldSetThemToZeroTest() {
        Floor floor1 = new Floor(1.1, -1);
        assertEquals(0, floor1.getArea(), TOLERANCE);
        Floor floor2 = new Floor(-1.1, 111111111);
        assertEquals(0, floor2.getArea(), TOLERANCE);
        Floor floor3 = new Floor(-1, -1);
        assertEquals(0, floor3.getArea(), TOLERANCE);
    }

    @Test
    public void getCarpetCostPerSquareMeterTest() {
        Carpet carpet = new Carpet(240.00);
        assertEquals(240.00, carpet.getCost(), TOLERANCE);
    }

    @Test
    public void settingNegativeCostShouldSetItToZeroTest() {
        Carpet carpet = new Carpet(-240.00);
        assertEquals(0.0, carpet.getCost(), TOLERANCE);
    }

    @Test
    public void calculateTotalCostOfCarpettingTest() {
        Floor floor = new Floor(1,3);
        Carpet carpet = new Carpet(240.00);
        Calculator calculator = new Calculator(floor, carpet);
        assertEquals(720.0, calculator.getTotalCost(), TOLERANCE);
    }
}
