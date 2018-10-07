package Chapter_02;

import org.junit.Test;

import java.util.LinkedList;
import java.util.List;

import static org.junit.Assert.assertEquals;

public class Filter_tests {
    LinkedList<Apple> inventory = new LinkedList<>();

    private void initializeTestData() {
        inventory.add(new Apple(100, "green"));
        inventory.add(new Apple(100, "green"));
        inventory.add(new Apple(100, "green"));
        inventory.add(new Apple(100, "red"));
        inventory.add(new Apple(100, "brown"));
    }

    @Test
    public void testFilterGreenApples() {
        initializeTestData();
        List<Apple> fiteredApples = Filters.greenApples(inventory);
        assertEquals("Unexpected amount of filtered apples", 3, fiteredApples.size());
    }

    @Test
    public void testFilteringByColor() {
        initializeTestData();
        assertEquals("Unexpected amount of filtered apples", 1, Filters.applesByColor(inventory, "brown").size());
        assertEquals("Unexpected amount of filtered apples", 1, Filters.applesByColor(inventory, "red").size());
        assertEquals("Unexpected amount of filtered apples", 3, Filters.applesByColor(inventory, "green").size());
    }

    @Test
    public void testFilteringHeavyAndRed() {
        initializeTestData();
        inventory.add(new Apple(200, "blue"));
        inventory.add(new Apple(200, "red"));
        assertEquals("Unexpected amount of filtered apples", 1, Filters.applesByPredicate(inventory, new AppleRedAndHeavyPredicate()).size());
    }
}
