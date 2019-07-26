class LuhnValidator {

    boolean isValid(String candidate) {
        candidate = candidate.replaceAll("\\s", "");
        candidate = new StringBuilder(candidate).reverse().toString();

        if(candidate.length() <= 1) return false;

        int sumOfDigits = 0;
        for (int i = 0; i < candidate.length(); i++) {
            Character currentChar = candidate.charAt(i);
            if(!Character.isDigit(currentChar)) return false;

            int digit = Character.getNumericValue(currentChar);
            if (i % 2 == 0) {
                sumOfDigits += digit;
            } else {
                sumOfDigits += (digit * 2 > 9) ? (digit * 2 - 9) : (digit * 2);
            }
        }

        if (sumOfDigits % 10 == 0) return true;

        return false;
    }

}
