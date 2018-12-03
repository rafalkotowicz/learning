package section_05.exercises;

public class GreatestCommonDivisor {
    public static int getGreatestCommonDivisor(int first, int second) {
        if (first < 10 || second < 10) {
            return -1;
        }

        int maxDivisor = 0;
        int maxCycles = Math.min(first, second);
        for (int i = 1; i <= maxCycles; i++) {
            if (first % i == 0 && second % i == 0) {
                maxDivisor = i;
            }
        }

        return maxDivisor;
    }
}
