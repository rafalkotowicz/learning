package section_04.exercises;

public class DecimalComparator {
    public static boolean areEqualByThreeDecimalPlaces(double a, double b) {
        return (Math.abs(a - b) < 0.0009);
    }
}
