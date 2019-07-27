package Chapter_02;

import org.junit.Test;

import java.util.LinkedList;

import static Chapter_02.PrettyPrinter.*;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

public class PrettyPrintTest {
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
    public void fancyFormatterTest() {
        initializeTestData();

        final String expected = "A light green apple.\n" +
                "A light green apple.\n" +
                "A light green apple.\n" +
                "A light red apple.\n" +
                "A light brown apple.\n" +
                "A heavy blue apple.\n" +
                "A light red apple.\n" +
                "A heavy red apple.\n" +
                "A heavy red apple.\n";

         assertTrue("Unexpected pretty print output", expected.equals(print(inventory, new FancyFormatter())));
    }

    @Test
    public void colortFormatterTest() {
        initializeTestData();

        final String expected = "A green apple.\n" +
                "A green apple.\n" +
                "A green apple.\n" +
                "A red apple.\n" +
                "A brown apple.\n" +
                "A blue apple.\n" +
                "A red apple.\n" +
                "A red apple.\n" +
                "A red apple.\n";

        assertTrue("Unexpected pretty print output", expected.equals(print(inventory, new ColorFormatter())));
    }

    @Test
    public void simpleWeightFormatterTest() {
        initializeTestData();

        final String expected = "An apple weighting 100 grams.\n" +
                "An apple weighting 100 grams.\n" +
                "An apple weighting 100 grams.\n" +
                "An apple weighting 100 grams.\n" +
                "An apple weighting 100 grams.\n" +
                "An apple weighting 200 grams.\n" +
                "An apple weighting 150 grams.\n" +
                "An apple weighting 200 grams.\n" +
                "An apple weighting 210 grams.\n";

        assertTrue("Unexpected pretty print output", expected.equals(print(inventory, new SimpleWeightFormatter())));
    }
}
