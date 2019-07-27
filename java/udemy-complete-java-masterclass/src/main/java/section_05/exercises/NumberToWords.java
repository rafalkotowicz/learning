package section_05.exercises;

public class NumberToWords {
    public static int getDigitCount(int number) {
        if (number < 0) {
            return -1;
        }
        if (number == 0) {
            return 1;
        }

        for (int i = 0; ; i++) {
            if (number > 0) {
                number /= 10;
            } else {
                return i;
            }
        }
    }

    public static int reverse(int number) {
        boolean isNegative = number < 0;
        number = Math.abs(number);
        int result = 0;
        int maxCycles = getDigitCount(number);
        for (int i = 1; i <= maxCycles; i++) {
            result += (number % 10) * Math.pow(10, maxCycles - i);
            number /= 10;
        }

        return isNegative ? -result : result;
    }

    public static void numberToWords(int number) {
        if (number < 0) {
            System.out.print("Invalid Value ");
        }

        final int maxCycles = getDigitCount(number);
        number = reverse(number);

        for (int i = 1; i <= maxCycles; i++) {
            switch (number % 10) {
                case 0:
                    System.out.print("Zero");
                    break;
                case 1:
                    System.out.print("One");
                    break;
                case 2:
                    System.out.print("Two");
                    break;
                case 3:
                    System.out.print("Three");
                    break;
                case 4:
                    System.out.print("Four");
                    break;
                case 5:
                    System.out.print("Five");
                    break;
                case 6:
                    System.out.print("Six");
                    break;
                case 7:
                    System.out.print("Seven");
                    break;
                case 8:
                    System.out.print("Eight");
                    break;
                case 9:
                    System.out.print("Nine");
                    break;
                default:
                    System.out.print("Are you sure you are using decimal system?");
                    break;
            }
            number /= 10;
            System.out.print(" ");
        }
    }
}
