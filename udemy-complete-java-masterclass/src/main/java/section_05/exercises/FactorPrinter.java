package section_05.exercises;

public class FactorPrinter {
    public static String findFactors(int number) {
        if (number < 1) {
            return "Invalid Value";
        }

        StringBuilder factors = new StringBuilder();
        for (int i = 1; i <= number; i++) {
            if (number % i == 0) {
                factors.append(i).append(" ");
            }
        }

        return factors.toString().trim();
    }

    public static void printFactors(int number) {
        System.out.println(findFactors(number));
    }
}
