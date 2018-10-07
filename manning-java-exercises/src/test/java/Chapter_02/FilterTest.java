package Chapter_02;

import org.junit.Test;

import java.util.LinkedList;
import java.util.List;

import static Chapter_02.Filters.applesByColor;
import static Chapter_02.Filters.applesByPredicate;
import static Chapter_02.Filters.greenApples;
import static org.junit.Assert.assertEquals;

public class FilterTest {
    LinkedList<Apple> inventory = new LinkedList<>();

    private void initializeTestData() {
        inventory.add(new Apple(100, "green"));
        inventory.add(new Apple(100, "green"));
        inventory.add(new Apple(100, "green"));
        inventory.add(new Apple(100, "red"));
        inventory.add(new Apple(100, "brown"));
        inventory.add(new Apple(200, "blue"));
        inventory.add(new Apple(150, "red"));
        inventory.add(new Apple(200, "red"));
        inventory.add(new Apple(210, "red"));
    }

    @Test
    public void testFilterGreenApples() {
        initializeTestData();
        List<Apple> fiteredApples = greenApples(inventory);
        assertEquals("Unexpected amount of filtered apples", 3, fiteredApples.size());
    }

    @Test
    public void testFilteringByColor() {
        initializeTestData();
        assertEquals("Unexpected amount of filtered apples", 1, applesByColor(inventory, "brown").size());
        assertEquals("Unexpected amount of filtered apples", 4, applesByColor(inventory, "red").size());
        assertEquals("Unexpected amount of filtered apples", 3, applesByColor(inventory, "green").size());
    }

    @Test
    public void testFilteringHeavyAndRed() {
        initializeTestData();
        assertEquals("Unexpected amount of filtered apples", 2, applesByPredicate(inventory, new AppleRedAndHeavyPredicate()).size());
    }
}
