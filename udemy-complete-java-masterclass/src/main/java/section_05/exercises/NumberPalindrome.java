package section_05.exercises;

    public class NumberPalindrome {
        public static boolean isPalindrome(int number) {
            int unsignedNumber = Math.abs(number);

            String inNumber = String.valueOf(unsignedNumber);
            for (int i = 0; i < inNumber.length()/2; i++) {
                char currentChar = inNumber.charAt(i);
                char complementaryChar = inNumber.charAt(inNumber.length() - i - 1);
                if (currentChar != complementaryChar) {
                    return false;
                }
            }
            return true;
        }
    }
