package Chapter_02;

import java.util.LinkedList;
import java.util.List;

public class Filters {
    public static List<Apple> greenApples(List<Apple> appleInventory) {
        LinkedList<Apple> result = new LinkedList<Apple>();
        for (Apple apple : appleInventory) {
            if("green".equalsIgnoreCase(apple.color)) result.add(apple);
        }
        return result;
    }

    public static List<Apple> applesByColor(List<Apple> appleInventory, String color) {
        LinkedList<Apple> result = new LinkedList<Apple>();
        for (Apple apple : appleInventory) {
            if(color.equalsIgnoreCase(apple.color)) result.add(apple);
        }
        return result;
    }

    public static List<Apple> applesByPredicate(List<Apple> appleInventory, ApplePredicate ap) {
        LinkedList<Apple> result = new LinkedList<Apple>();
        for (Apple apple : appleInventory) {
            if(ap.test(apple)) result.add(apple);
        }
        return result;
    }
}
