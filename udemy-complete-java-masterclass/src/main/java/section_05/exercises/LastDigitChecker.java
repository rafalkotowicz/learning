package section_05.exercises;

public class LastDigitChecker {

    public static boolean hasSameLastDigit(int a, int b, int c) {
        if (a < 10 || a > 1000 || b < 10 || b > 1000 || c < 10 || c > 1000) {
            return false;
        }

        int ald = a % 10;
        int bld = b % 10;
        int cld = c % 10;

        if(ald == bld || bld == cld || ald == cld) {
            return true;
        }
        return false;
    }
}
