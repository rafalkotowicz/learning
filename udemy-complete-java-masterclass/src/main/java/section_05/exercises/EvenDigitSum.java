package section_05.exercises;

public class EvenDigitSum {

    public static int getEvenDigitSum(int number) {
        if (number < 0) {
            return -1;
        }

        int eventDigitSum = 0;
        while (number > 0) {
            int currentDigit = number % 10;
            if (currentDigit % 2 == 0) {
                eventDigitSum += currentDigit;
            }
            number /= 10;
        }

        return eventDigitSum;
    }
}
