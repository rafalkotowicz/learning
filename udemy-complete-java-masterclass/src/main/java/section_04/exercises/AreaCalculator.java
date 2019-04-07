package section_04.exercises;

public class AreaCalculator {

    public static double area(double radius) {
        final double PI = 3.141592;
        return radius >= 0 ? PI * radius * radius : -1.0d;
    }

    public static double area(double x, double y) {
        return x >= 0 && y >= 0 ? x * y : -1.0d;
    }
}
