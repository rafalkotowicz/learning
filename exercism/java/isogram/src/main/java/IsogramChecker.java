import java.util.HashSet;

class IsogramChecker {

    boolean isIsogram(String phrase) {
        phrase = normalizePhrase(phrase);

        HashSet<Character> lettersUsed = new HashSet<>();

        for (int i = 0; i < phrase.length(); i++) {
            lettersUsed.add(phrase.charAt(i));
        }

        return lettersUsed.size() == phrase.length();
    }

    private String normalizePhrase(String phrase) {
        String normalized = phrase.toLowerCase();
        normalized = normalized.replaceAll("[ -]", "");
        return normalized;
    }

}
