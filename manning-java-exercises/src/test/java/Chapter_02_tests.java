import Chapter_02.Apple;
import org.junit.Test;

import java.util.LinkedList;

public class Chapter_02_tests {

    @Test
    public void testFilterBigApples() {
        LinkedList<Apple> inventory = new LinkedList<>();
        for (int i = 100; i <= 300; i++) {
            inventory.add(new Apple(i, "green"));
        }

        int expectedApples = 1;
        int actualApples =

        assertEquals("Unexpected number of filtered apples. Expected: " + 1 + ". Actual: " + 0 "")
    }
}
