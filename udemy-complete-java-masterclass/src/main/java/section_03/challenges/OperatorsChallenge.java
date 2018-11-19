package section_03.challenges;

public class OperatorsChallenge {
    public static boolean isLowerOrEqualToLimit(double a, double b, int multiplyBy, int divideBy, int limit) {
        final int reminder = (int)(((a + b) * multiplyBy) % divideBy);
        return (reminder <= limit) ? true : false;
    }
}
