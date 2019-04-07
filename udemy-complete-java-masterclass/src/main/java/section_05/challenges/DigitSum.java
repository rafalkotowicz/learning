package section_05.challenges;

public class DigitSum {
    public static int sumDigits(int number) {
        if (number <= 9) {
            return -1;
        }
        int result = 0;
        String asString = Integer.toString(number);
        for (char c : asString.toCharArray()) {
            result += Integer.valueOf(Character.toString(c));
        }

        return result;
    }

    public static int sumDigits2(int number) {
        if (number <= 9) {
            return -1;
        }
        int result = 0;

        while (number > 0) {
            result += number % 10;
            number = number / 10;
        }

        return result;
    }
}
