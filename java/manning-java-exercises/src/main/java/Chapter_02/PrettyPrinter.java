package Chapter_02;

import java.util.List;

public class PrettyPrinter {
    public static String print(List<Apple> inventory, AppleFormatter af) {
        StringBuilder result = new StringBuilder();
        for(Apple apple : inventory) {
            result.append(af.accept(apple)).append("\n");
        }
        return result.toString();
    }
}
