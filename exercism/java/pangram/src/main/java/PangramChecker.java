import java.util.HashMap;
import java.util.Map;

public class PangramChecker {
    private static final short noOfLettersInLatinAlphabet = 26;

    public boolean isPangram(String input) {
        if(input == null) {
            throw new NullPointerException("Invalid Input");
        }

        if(input.isEmpty()) {
            return false;
        }

        input = input.toLowerCase();
        Map uniqueLetters = new HashMap<Character, Boolean>();
        for(int i = 0; i < input.length(); i++) {
            if (Character.isLetter(input.charAt(i))) {
                uniqueLetters.put(input.charAt(i), true);
            }
        }

        if(uniqueLetters.size() == noOfLettersInLatinAlphabet) {
            return true;
        } else {
            return false;
        }
    }
}
