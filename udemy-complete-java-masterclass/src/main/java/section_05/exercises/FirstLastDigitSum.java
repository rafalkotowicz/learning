package section_05.exercises;

public class FirstLastDigitSum {

    public static int sumFirstAndLastDigit(int number) {
        if (number < 0) {
            return -1;
        }

        int firstDigit = number % 10;
        int lastDigit = 0;

        while (number > 0) {
            lastDigit = number;
            number /= 10;
        }

        return firstDigit + lastDigit;
    }
}
