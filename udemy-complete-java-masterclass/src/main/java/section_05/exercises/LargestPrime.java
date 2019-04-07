package section_05.exercises;

public class LargestPrime {
    public static int getLargestPrime(final int number) {
        if (number < 2) {
            return -1;
        }

        int largestPrimeFound = -1;
        for (int i = 1; i <= number; i++) {
            if (number % i == 0 && isPrime(i)) {
                largestPrimeFound = i;
            }
        }
        return largestPrimeFound;
    }

    private static boolean isPrime(final int number) {
        for (long y = 2; y <= Math.sqrt(number); y++) {
            if (number % y == 0) {
                return false;
            }
        }
        return true;
    }
}
