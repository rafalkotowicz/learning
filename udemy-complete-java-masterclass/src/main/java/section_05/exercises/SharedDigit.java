package section_05.exercises;

public class SharedDigit {
    public static boolean hasSharedDigit(int a, int b) {
        if ( a < 10 || a > 99 || b < 10 || b >99) {
            return false;
        }

        for(int i = a; i>0; i/=10) {
            for(int j = b; j>0; j/=10) {
                int currentDigitInA = i % 10;
                int currentDigitInB = j % 10;
                if (currentDigitInA == currentDigitInB) {
                    return true;
                }
            }
        }

        return false;
    }
}
