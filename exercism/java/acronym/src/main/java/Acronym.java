class Acronym {
    private String phrase;

    Acronym(String phrase) {
        this.phrase = phrase;
    }

    String get() {
        String[] words = phrase.split("[ -]");
        StringBuilder acronym = new StringBuilder();
        for (String word : words) {
            acronym.append(word.charAt(0));
        }
        return acronym.toString().toUpperCase();
    }

}
