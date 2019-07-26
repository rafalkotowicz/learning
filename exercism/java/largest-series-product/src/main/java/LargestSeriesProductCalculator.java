import java.util.regex.Matcher;
import java.util.regex.Pattern;

class LargestSeriesProductCalculator {
    private final String inputNumber;

    LargestSeriesProductCalculator(String inputNumber) {
        if (inputNumber == null) throw new IllegalArgumentException("String to search must be non-null.");

        Pattern onlyDigits = Pattern.compile("[0-9]*");
        Matcher matcher = onlyDigits.matcher(inputNumber);

        if (matcher.matches()) {
            this.inputNumber = inputNumber;
        } else {
            throw new IllegalArgumentException("String to search may only contain digits.");
        }
    }

    long calculateLargestProductForSeriesLength(int numberOfDigits) {
        if (numberOfDigits > inputNumber.length())
            throw new IllegalArgumentException("Series length must be less than or equal to the length of the string to search.");
        if (numberOfDigits < 0)
            throw new IllegalArgumentException("Series length must be non-negative.");

        long largestProduct = 0;
        for (int i = 0; i < inputNumber.length() - numberOfDigits + 1; i++) {
            String window = inputNumber.substring(i, i + numberOfDigits);
            long product = 1;
            for (int j = 0; j < window.length(); j++) {
                product *= Character.getNumericValue(window.charAt(j));
            }

            largestProduct = (product > largestProduct) ? product : largestProduct;
        }
        return largestProduct;
    }
}
