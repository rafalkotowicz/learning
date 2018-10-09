package Chapter_02;

import org.junit.Before;
import org.junit.Test;

import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;

import static Chapter_02.Filters.*;
import static Chapter_02.PrettyPrinter.print;
import static org.junit.Assert.assertEquals;

public class FilterTest {
    LinkedList<Apple> inventory = new LinkedList<>();
    final String sortedInventory;

    {
        sortedInventory = "An apple weighting 100 grams.\n" +
                "An apple weighting 100 grams.\n" +
                "An apple weighting 101 grams.\n" +
                "An apple weighting 103 grams.\n" +
                "An apple weighting 105 grams.\n" +
                "An apple weighting 150 grams.\n" +
                "An apple weighting 200 grams.\n" +
                "An apple weighting 200 grams.\n" +
                "An apple weighting 210 grams.\n";
    }

    @Before
    public void initializeTestData() {
        inventory.add(new Apple(105, "green"));
        inventory.add(new Apple(103, "green"));
        inventory.add(new Apple(101, "green"));
        inventory.add(new Apple(150, "red"));
        inventory.add(new Apple(100, "red"));
        inventory.add(new Apple(100, "brown"));
        inventory.add(new Apple(200, "blue"));
        inventory.add(new Apple(200, "red"));
        inventory.add(new Apple(210, "red"));
    }

    @Test
    public void testFilterGreenApples() {
        assertEquals("Unexpected amount of filtered apples", 3, greenApples(inventory).size());
    }

    @Test
    public void testFilteringByColor() {
        assertEquals("Unexpected amount of filtered apples", 1, applesByColor(inventory, "brown").size());
        assertEquals("Unexpected amount of filtered apples", 4, applesByColor(inventory, "red").size());
        assertEquals("Unexpected amount of filtered apples", 3, applesByColor(inventory, "green").size());
    }

    @Test
    public void testFilteringHeavyAndRed() {
        assertEquals("Unexpected amount of filtered apples", 2, applesByPredicate(inventory, new AppleRedAndHeavyPredicate()).size());
    }

    @Test
    public void testAnonymousClassPredicate() {
        assertEquals("Unexpected amount of filtered apples", 2, applesByPredicate(inventory, new ApplePredicate() {
            public boolean test(Apple apple) {
                return "red".equals(apple.color) && apple.weight > 150;
            }
        }).size());
    }

    @Test
    public void testFirstLambdaApproach() {
        assertEquals("Unexpected amount of filtered apples", 1, applesByPredicate(inventory, (Apple a) -> "brown".equals(a.color)).size());
        assertEquals("Unexpected amount of filtered apples", 4, applesByPredicate(inventory, (Apple a) -> "red".equals(a.color)).size());
        assertEquals("Unexpected amount of filtered apples", 3, applesByPredicate(inventory, (Apple a) -> "green".equals(a.color)).size());
    }

    @Test
    public void testAbstractingListTypeAndPredicate() {
        assertEquals("Unexpected amount of filtered apples", 1, genericFilter(inventory, (Apple a) -> "brown".equals(a.color)).size());
        assertEquals("Unexpected amount of filtered apples", 4, genericFilter(inventory, (Apple a) -> "red".equals(a.color)).size());
        assertEquals("Unexpected amount of filtered apples", 3, genericFilter(inventory, (Apple a) -> "green".equals(a.color)).size());
    }

    @Test
    public void testSortingWithoutLambdaComparator() {
        inventory.sort(new Comparator<Apple>() {
            @Override
            public int compare(Apple a1, Apple a2) {
                if(a1.weight < a2.weight) return -1;
                if(a1.weight == a2.weight) return 0;
                if(a1.weight > a2.weight) return 1;
                throw new RuntimeException("This message should never be seen. Something went terribly wrong");
            }
        });
        assertEquals("Sorting unsuccessful :(", sortedInventory, print(inventory, new SimpleWeightFormatter()));
    }

    @Test
    public void testSortingWithLambdaComparator() {
        inventory.sort((Apple a1, Apple a2) -> a1.getWeight().compareTo(a2.getWeight()));
        assertEquals("Sorting unsuccessful :(", sortedInventory, print(inventory, new SimpleWeightFormatter()));
    }

    @Test
    public void testSortingWithMethodReference() {
        inventory.sort(Comparator.comparing(Apple::getWeight));
        assertEquals("Sorting unsuccessful :(", sortedInventory, print(inventory, new SimpleWeightFormatter()));
    }
}
