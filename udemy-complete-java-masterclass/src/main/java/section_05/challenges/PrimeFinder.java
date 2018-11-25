package section_05.challenges;

import java.util.ArrayList;
import java.util.List;

public class PrimeFinder {
    public static boolean isPrime(long number) {
        if (number < 1) return false;

        if (1 == number) {
            return false;
        }
        for (long i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static List<Integer> find(int start, int end) {
        List<Integer> results = new ArrayList<>();
        for (int i = start; i <= end; i++) {
            if (isPrime(i)) {
                results.add(i);
            }
            if (results.size() >= 3) {
                break;
            }
        }
        return results;
    }
}
